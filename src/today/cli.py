import sys
from datetime import datetime

from today import DiaryDate


def main():
    diary = DiaryDate()
    args = sys.argv[1:]

    if not args or args == ["today"]:
        print(diary.filepath(datetime.today(), create=True))
    elif args == ["week"]:
        for path in diary.week_files():
            print(path)
    elif args == ["month"]:
        for path in diary.month_files():
            print(path)
    else:
        dt = diary.parse(" ".join(args))
        print(diary.filepath(dt))
