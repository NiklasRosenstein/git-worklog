## git-timetrack

Track work times in a separate `timetracking` branch.

### Synopsis

```
usage: git-timetrack abort [-h]

Abort the current session.

optional arguments:
  -h, --help  show this help message and exit
```

```
usage: git-timetrack [-h] {checkin,checkout,show,status} ...

Allows you to track working times in a separate `timetracking` branch.

positional arguments:
  {checkin,checkout,show,status}

optional arguments:
  -h, --help            show this help message and exit
```

```
usage: git-timetrack checkin [-h] [--time TIME]

Checks you in to start a local time-tracking session.

optional arguments:
  -h, --help   show this help message and exit
  --time TIME  Override check-in time.
```

```
usage: git-timetrack checkpoint [-h] [-m MESSAGE] [--time TIME]

Commit a new log from the current session and start a new one.

optional arguments:
  -h, --help            show this help message and exit
  -m MESSAGE, --message MESSAGE
                        A message for the log.
  --time TIME           Override check-out and new check-in time.
```

```
usage: git-timetrack checkout [-h] [-m MESSAGE] [--time TIME]

Checks you out an adds an entry to your timetable file in the timetracking
branch.

optional arguments:
  -h, --help            show this help message and exit
  -m MESSAGE, --message MESSAGE
                        A message for the log.
  --time TIME           Override check-out time.
```

```
usage: git-timetrack show [-h] [--user USER]

Prints your timetable (or that of the specified user). The timetable is a TSV
file with the three columns CHECKINTIME, CHECKOUTTIME and MESSAGE. All times
have timezone information attached.

optional arguments:
  -h, --help   show this help message and exit
  --user USER  User to retrieve the timetable for.
```

```
usage: git-timetrack status [-h]

Displays your current session, that is the time passed since checkin or
otherwise that there is no active time-tracking session.

optional arguments:
  -h, --help  show this help message and exit
```
