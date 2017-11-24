# Copyright (c) 2017 Niklas Rosenstein
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from __future__ import print_function
import argparse
import io
import os
import sys

if 'require' in globals():
  git = require('./git')
  timetable = require('./timetable')
else:
  from . import git, timetable


parser = argparse.ArgumentParser(prog='git-timetrack', description="""
  Allows you to track working times in a separate `timetracking` branch.
""")
subparsers = parser.add_subparsers(dest='command')

checkin_parser = subparsers.add_parser('checkin', description="""
  Checks you in to start a local time-tracking session.
""")
checkin_parser.add_argument('--time', type=timetable.parse_time, help='Override check-in time.')

checkout_parser = subparsers.add_parser('checkout', description="""
  Checks you out an adds an entry to your timetable file in the timetracking
  branch.
""")
checkout_parser.add_argument('-m', '--message', help='A message for the log.')
checkout_parser.add_argument('--time', type=timetable.parse_time, help='Override check-out time.')

status_parser = subparsers.add_parser('status', description="""
  Displays your current session, that is the time passed since checkin or
  otherwise that there is no active time-tracking session.
""")

show_parser = subparsers.add_parser('show', description="""
  Prints your timetable (or that of the specified user). The timetable is a
  TSV file with the three columns CHECKINTIME, CHECKOUTTIME and MESSAGE.
  All times have timezone information attached.
""")
show_parser.add_argument('--user', help='User to retrieve the timetable for.')


def print_err(*message):
  print(*message, file=sys.stderr)


def checkin(time):
  try:
    data = timetable.get_checkin()
  except timetable.NoCheckinAvailable:
    pass
  else:
    print_err('fatal: already checked in: {} at {}'.format(data.name, timetable.strftime(data.time)))
    print_err('       did you forget to check out, last time? ')
    print_err('       use the --time argument on checkout.')
    return 1

  user_name = git.config('user.name')
  if not user_name:
    print_err('fatal: user.name not configured.')
    return 1

  data = timetable.set_checkin(user_name, time)
  print('checked in: {} at {}'.format(data.name, timetable.strftime(data.time)))


def checkout(message, time):
  try:
    checkin = timetable.get_checkin()
  except timetable.NoCheckinAvailable:
    print_err('fatal: not checked-in')
    return 1

  time = time or timetable.now()
  if time <= checkin.time:
    print_err('fatal: check-out time can not be at a point in time before check-in.')
    return 1

  data = timetable.add_checkout(checkin.name, checkin.time, time, message)
  timetable.rem_checkin()
  print('checked out: {}, interval is {}'.format(checkin.name, str(data.interval)))


def status():
  try:
    data = timetable.get_checkin()
  except timetable.NoCheckinAvailable:
    print('not checked in.')
  else:
    h, m, s = timetable.splittimedelta(timetable.now() - data.time, 'HMS')
    info = '{} seconds'.format(s)
    if m > 0: info = '{} minutes and {}'.format(m, info)
    if h > 0: info = '{} hours, {}'.format(h, info)
    print('{} at {} (since {})'.format(data.name,
        timetable.strftime(data.time), info))


def show(user):
  user = user or git.config('user.name')
  try:
    print(git.show('{}:{}.tsv'.format(timetable.BRANCH, user)))
  except git.DoesNotExist as exc:
    print_err(exc)
    return 1


def main(argv=None):
  args = parser.parse_args(argv)
  if not args.command:
    parser.print_usage()
    return 0
  elif args.command == 'checkin':
    return checkin(args.time)
  elif args.command == 'checkout':
    return checkout(args.message, args.time)
  elif args.command == 'show':
    return show(args.user)
  elif args.command == 'status':
    return status()
  else:
    print('fatal: invalid command {}'.format(args.command), file=sys.stderr)
    return 128


if ('require' in globals() and require.main == module) or __name__ == '__main__':
  sys.exit(main())
