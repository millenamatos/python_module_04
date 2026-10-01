import sys
from typing import IO


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: ft_ancient_text.py <file>")
        sys.exit(1)

    filename: str = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    try:
        file: IO[str] = open(filename, "r")
        content: str = file.read()

        print(f"---\n{content} \n---")
        file.close()

        print(f"File '{filename}' closed.")

    except FileNotFoundError as error:
        print(f"Error opening file '{filename}': {error}")
    except PermissionError as error:
        print(f"Error opening file '{filename}': {error}")


if __name__ == "__main__":
    main()