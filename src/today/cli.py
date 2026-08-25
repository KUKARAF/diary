import sys
from datetime import datetime

from today import DiaryDate

USAGE = """\
Usage: diary [WHEN]

Print the path to a diary entry, creating today's file if it is missing.

  diary                today's entry
  diary today          same as above
  diary week           every entry in the current week
  diary month          every entry in the current month
  diary WHEN           natural-language date, e.g. "tomorrow",
                       "last friday", "3 days ago"

Options:
  -h, --help           show this message and exit
"""


def main():
    args = sys.argv[1:]

    # Checked before anything else: every remaining argument is treated as a
    # date expression, so a flag would otherwise be handed to the parser and
    # come back as an unhandled ValueError.
    if args and args[0] in ("-h", "--help"):
        print(USAGE, end="")
        return 0

    diary = DiaryDate()

    if not args or args == ["today"]:
        print(diary.filepath(datetime.today(), create=True))
    elif args == ["week"]:
        for path in diary.week_files():
            print(path)
    elif args == ["month"]:
        for path in diary.month_files():
            print(path)
    else:
        try:
            dt = diary.parse(" ".join(args))
        except ValueError as exc:
            print(f"diary: {exc}", file=sys.stderr)
            print('Try "diary --help" for usage.', file=sys.stderr)
            return 1
        print(diary.filepath(dt))

    return 0
