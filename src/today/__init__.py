import calendar
from datetime import datetime, timedelta
from pathlib import Path

from today.config import load_config
from today.kv import KVManager


class DiaryDate:
    """Resolve dates to diary file paths and parse natural language dates."""

    def __init__(self, diary_dir=None, extension=None):
        config = load_config()
        self.diary_dir = Path(diary_dir or config["diary"]["directory"]).expanduser()
        self.extension = extension or config["diary"]["extension"]

    def filepath(self, dt: datetime, create: bool = False) -> Path:
        """Convert a datetime to a diary file path. Optionally create the file."""
        path = self.diary_dir / f"{dt:%Y-%m-%d}{self.extension}"
        if create and not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.touch()
        return path

    def week_files(self) -> list[Path]:
        """Return existing diary file paths for the current week (Mon–Sun)."""
        today = datetime.now()
        monday = today - timedelta(days=today.weekday())
        files = []
        for i in range(7):
            path = self.filepath(monday + timedelta(days=i))
            if path.exists():
                files.append(path)
        return files

    def month_files(self) -> list[Path]:
        """Return existing diary file paths for the current month."""
        now = datetime.now()
        days_in_month = calendar.monthrange(now.year, now.month)[1]
        files = []
        for day in range(1, days_in_month + 1):
            path = self.filepath(datetime(now.year, now.month, day))
            if path.exists():
                files.append(path)
        return files

    def parse(self, text: str) -> datetime:
        """Parse natural language date string into a datetime."""
        from timefhuman import timefhuman, tfhConfig

        config = tfhConfig(now=datetime.now())
        results = timefhuman(text, config=config)
        if not results:
            raise ValueError(f"Could not parse: {text}")
        result = results[0]
        if isinstance(result, tuple):
            return result[0]
        if isinstance(result, list):
            return result[0]
        return result
