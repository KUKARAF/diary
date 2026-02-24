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
