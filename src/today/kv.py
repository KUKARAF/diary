import os


class KVManager:
    """Read/write YAML frontmatter key-value pairs in markdown files."""

    @staticmethod
    def read_frontmatter(file_path: str) -> dict:
        """Parse YAML frontmatter from a markdown file."""
        if not os.path.exists(file_path):
            return {}

        with open(file_path, "r") as f:
            content = f.read()

        if not content.startswith("---"):
            return {}

        try:
            parts = content.split("---", 2)
            if len(parts) < 3:
                return {}

            frontmatter_text = parts[1].strip()
            data = {}

            for line in frontmatter_text.split("\n"):
                if ":" in line:
                    key, value = line.split(":", 1)
                    key = key.strip()
                    value = value.strip()

                    if value.isdigit():
                        value = int(value)

                    data[key] = value

            return data
        except Exception:
            return {}

    @staticmethod
    def write_frontmatter(file_path: str, data: dict) -> None:
        """Write YAML frontmatter to a markdown file, preserving content below."""
        content = ""
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                content = f.read()

        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                content = parts[2].lstrip("\n")
            else:
                content = ""

        frontmatter_lines = ["---"]
        for key in sorted(data.keys()):
            frontmatter_lines.append(f"{key}: {data[key]}")
        frontmatter_lines.append("---")
        frontmatter_lines.append("")

        with open(file_path, "w") as f:
            f.write("\n".join(frontmatter_lines))
            if content:
                f.write("\n" + content)

    def get(self, file_paths: list[str], key: str) -> int | str:
        """Get value for key. Averages across files if numeric."""
        values = []
        for file_path in file_paths:
            data = self.read_frontmatter(file_path)
            if key in data:
                values.append(data[key])

        if values and all(isinstance(v, (int, float)) for v in values):
            average = sum(values) / len(values)
            if average == int(average):
                return int(average)
            return round(average, 2)
        elif values:
            return values[0]
        return 0

    def set(self, file_path: str, key: str, value) -> None:
        """Set key to value."""
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        data = self.read_frontmatter(file_path)
        data[key] = value
        self.write_frontmatter(file_path, data)

    def add(self, file_path: str, key: str, value: int = 1) -> int:
        """Increment key by value. Returns new value."""
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        data = self.read_frontmatter(file_path)
        current = data.get(key, 0)
        if not isinstance(current, (int, float)):
            current = 0
        data[key] = current + value
        self.write_frontmatter(file_path, data)
        return data[key]

    def sub(self, file_path: str, key: str, value: int = 1) -> int:
        """Decrement key by value. Returns new value."""
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        data = self.read_frontmatter(file_path)
        current = data.get(key, 0)
        if not isinstance(current, (int, float)):
            current = 0
        data[key] = current - value
        self.write_frontmatter(file_path, data)
        return data[key]
