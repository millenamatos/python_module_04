import sys
from typing import IO


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: ft_stream_management.py <file>")
        return

    filename: str = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    try:
        file: IO[str] = open(filename)
        content: str = file.read()
        print(f"---\n\n{content}\n\n---")
        file.close()
        print(f"File '{filename}' closed.\n")

        lines: list[str] = content.splitlines()
        transformed: str = "\n".join(line + "#" for line in lines)
        print("Transform data:")
        print(f"---\n\n{transformed}\n\n---")
    except FileNotFoundError as error:
        print(f"[STDERR] Error opening file '{filename}': "
              f"{error}", file=sys.stderr)
        return
    except PermissionError as error:
        print(f"[STDERR] Error opening file '{filename}': "
              f"{error}", file=sys.stderr)
        return

    try:
        print("Enter new file name (or empty): ", end="")
        sys.stdout.flush()
        new_filename: str = sys.stdin.readline()
        new_filename = new_filename.strip('\n')
        if not new_filename:
            print("Not saving data.")
        else:
            print(f"Saving data to '{new_filename}'")
            output_file: IO[str] = open(new_filename, "w")
            output_file.write(transformed)
            output_file.close()
            print(f"Data saved in file '{new_filename}'")
    except PermissionError as error:
        print(f"[STDERR] Error opening file '{new_filename}': "
              f"{error}", file=sys.stderr)
        print("Data not saved.")


if __name__ == "__main__":
    main()
