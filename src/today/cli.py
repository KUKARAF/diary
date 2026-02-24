import sys
from datetime import datetime

from today import DiaryDate


def main():
    diary = DiaryDate()
    args = sys.argv[1:]
    if not args:
        print(diary.filepath(datetime.today(), create=True))
    else:
        dt = diary.parse(" ".join(args))
        print(diary.filepath(dt))


def week():
    diary = DiaryDate()
    for path in diary.week_files():
        print(path)


def month():
    diary = DiaryDate()
    for path in diary.month_files():
        print(path)
