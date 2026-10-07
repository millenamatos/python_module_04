def secure_archive(
        filename: str,
        action: str = "read",
        content: str = ""
        ) -> tuple[bool, str]:
    try:
        if action == "read":
            with open(filename) as file:
                read_content = file.read()
                return (True, read_content)
        elif action == "write":
            with open(filename, "w") as file:
                file.write(content)
                return (True, "Content successfully written to file")
        else:
            return (False, "Error: Invalid action specified.")
    except FileNotFoundError as error:
        return (False, str(error))
    except PermissionError as error:
        return (False, str(error))


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))

    print("\nUsing 'secure_archive' to read from a regular file:")
    success, content = secure_archive("ancient_fragment.txt")
    print((success, content))

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive("preserved_archive.txt", "write", content))


if __name__ == "__main__":
    main()
