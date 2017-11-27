## git-worklog

Track work times in the `worklog` branch or in a separate repository.

### Configuration

* `worklog.repository` &ndash; If specified, must point to a Git repository
  on the filesystem. The `workworklog.project` option is required when this
  option is set. Usually, this option is defined in your global
  `~/.gitconfig` file.
* `worklog.project` &ndash; Defines the name of the branch that the work log
  is committed to. This is only used when `worklog.repository` is set.
* `worklog.branch` &ndash; Defines the name of the branch that the work log
  is commited to. This is only used when `worklog.repository` is *not* set.
  The default for this option is `worklog`.

### Time Formats

Git-worklog uses `%d/%b/%Y:%H:%M:%S %z` time format in the work log files.
However, some commands support one or more time options and typing a date in
the full time format is inconvenient, to say it frankly. Thus, these parameters
support the following time formats and will fill in the rest with the current
date and time.

See also: `git_worklog/timetable.py:parse_time()`

* `%H:%M`
* `%H:%M:%S`
* `%H-%M`
* `%H-%M-%S`
* `%d/%H:%M`
* `%d/%H:%M:%S`
* `%d` <sup>(1)</sup>
* `%d/%b` <sup>(1)</sup>
* `%m/%d/%H:%M`
* `%m/%d/%H:%M:%S`

<sup>(1)</sup> When using this time format, the daytime information will be
zeroed. Eg. `25/Nov` specifies the 25th of November in the current year at
0am.

### Synopsis

```
usage: git-worklog [-h] {checkin,checkout,show,status} ...

Allows you to track working times in a separate `worklog` branch.

positional arguments:
  {checkin,checkout,show,status}

optional arguments:
  -h, --help            show this help message and exit
```

```
usage: git-worklog abort [-h]

Abort the current session.

optional arguments:
  -h, --help  show this help message and exit
```

```
usage: git-worklog checkin [-h] [--time TIME]

Checks you in to start a local time-tracking session.

optional arguments:
  -h, --help   show this help message and exit
  --time TIME  Override check-in time.
```

```
usage: git-worklog checkpoint [-h] [-m MESSAGE] [--time TIME]

Commit a new log from the current session and start a new one.

optional arguments:
  -h, --help            show this help message and exit
  -m MESSAGE, --message MESSAGE
                        A message for the log.
  --time TIME           Override check-out and new check-in time.
```

```
usage: git-worklog checkout [-h] [-m MESSAGE] [--time TIME]

Checks you out an adds an entry to your timetable file in the worklog
branch.

optional arguments:
  -h, --help            show this help message and exit
  -m MESSAGE, --message MESSAGE
                        A message for the log.
  --time TIME           Override check-out time.
```

```
usage: git-worklog show [-h] [--user USER]

Prints your timetable (or that of the specified user). The timetable is a TSV
file with the three columns CHECKINTIME, CHECKOUTTIME and MESSAGE. All times
have timezone information attached.

optional arguments:
  -h, --help   show this help message and exit
  --user USER  User to retrieve the timetable for.
```

```
usage: git-worklog status [-h]

Displays your current session, that is the time passed since checkin or
otherwise that there is no active time-tracking session.

optional arguments:
  -h, --help  show this help message and exit
  -d, --detail
```
