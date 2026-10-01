import sys

def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: ft_ancient_text.py <file>")
        sys.exit(1)

    filename: str = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    try:
        file: str = open(filename)
        content: str = file.read()
        print(f"---\n{content}\n---")
        file.close()

        print(f"File '{filename}' closed.")
        lines: list[str] = content.splitlines()
        transformed: str = "\n".join(line + "#" for line in lines)
        print("Transform data:")
        print(f"---\n{transformed}\n---")
    except FileNotFoundError as error:
        print(f"[STDERR] Error opening file '{filename}': {error}", file=sys.stderr)
        sys.exit()
    except PermissionError as error:
        print(f"[STDERR] Error opening file '{filename}': {error}", file=sys.stderr)
        sys.exit()

    try:
        print("Enter new file name (or empty): ", end="")
        sys.stdout.flush()
        new_filename: str = sys.stdin.readline()
        new_filename: str = filename.strip('\n')
        if not new_filename:
            print("Not saving data.")
        else:
            print(f"Saving data to '{new_filename}'")
            output_file = open(new_filename, "w")
            output_file.write(transformed)
            output_file.close()
            print(f"Data saved in file '{new_filename}'")
    except PermissionError as error:
        print(f"[STDERR] Error opening file '{new_filename}': {error}", file=sys.stderr)
        print("Data not saved.")


if __name__ == "__main__":
    main()