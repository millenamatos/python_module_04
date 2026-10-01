import sys
from typing import IO


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: ft_ancient_text.py <file>")
        sys.exit(1)

    filename: str = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    try:
        file: IO[str] = open(filename, "r")
        content: str = file.read()
        print(f"---\n{content}\n---")
        file.close()

        print(f"File '{filename}' closed.")

        lines: list[str] = content.splitlines()
        transformed: str = "\n".join(line + "#" for line in lines)

        print("Transform data:")
        print(f"---\n{transformed}\n---")

        new_filename = input("Enter new file name (or empty): ")

        if not filename:
            print("Not saving data.")
        else:
            print(f"Saving data to '{new_filename}'")
            output_file: IO[str] = open(new_filename, "w")
            output_file.write(transformed + "\n")
            output_file.close()
            print(f"Data saved in file '{new_filename}'")

    except FileNotFoundError as error:
        print(f"Error opening file '{filename}': {error}") 
    except PermissionError as error:
        print(f"Error opening file '{filename}': {error}")


if __name__ == "__main__":
    main()