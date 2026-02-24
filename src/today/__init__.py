from datetime import datetime
from pathlib import Path

from today.config import load_config


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
