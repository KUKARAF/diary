import tomllib
from pathlib import Path

CONFIG_DIR = Path("~/.config/today").expanduser()
CONFIG_FILE = CONFIG_DIR / "config.toml"

DEFAULT_CONFIG = """\
[diary]
directory = "~/vimwiki/diary"
extension = ".md"
"""


def load_config() -> dict:
    if not CONFIG_FILE.exists():
        CONFIG_DIR.mkdir(parents=True, exist_ok=True)
        CONFIG_FILE.write_text(DEFAULT_CONFIG)
    return tomllib.loads(CONFIG_FILE.read_text())
