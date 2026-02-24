import sys

from today.kv import KVManager


def main():
    if len(sys.argv) < 3:
        print("Usage: kv_manager <operation> <key> [value]", file=sys.stderr)
        sys.exit(1)

    file_paths = []
    for line in sys.stdin:
        line = line.strip()
        if line:
            file_paths.append(line)

    if not file_paths:
        print("Error: No file paths provided via stdin", file=sys.stderr)
        sys.exit(1)

    operation = sys.argv[1]
    key = sys.argv[2]
    kv = KVManager()

    if operation == "get":
        print(kv.get(file_paths, key))
        return

    if len(file_paths) != 1:
        print(
            "Error: set, add, and sub operations require exactly one file path",
            file=sys.stderr,
        )
        sys.exit(1)

    file_path = file_paths[0]

    if operation == "set":
        if len(sys.argv) < 4:
            print("Error: set operation requires a value", file=sys.stderr)
            sys.exit(1)
        try:
            value = int(sys.argv[3])
        except ValueError:
            value = sys.argv[3]
        kv.set(file_path, key, value)
        print(value)

    elif operation == "add":
        value = 1
        if len(sys.argv) >= 4:
            try:
                value = int(sys.argv[3])
            except ValueError:
                print(
                    "Error: add operation requires a numeric value", file=sys.stderr
                )
                sys.exit(1)
        result = kv.add(file_path, key, value)
        print(result)

    elif operation == "sub":
        value = 1
        if len(sys.argv) >= 4:
            try:
                value = int(sys.argv[3])
            except ValueError:
                print(
                    "Error: sub operation requires a numeric value", file=sys.stderr
                )
                sys.exit(1)
        result = kv.sub(file_path, key, value)
        print(result)

    else:
        print(f"Error: Unknown operation '{operation}'", file=sys.stderr)
        print("Supported operations: get, set, add, sub", file=sys.stderr)
        sys.exit(1)
