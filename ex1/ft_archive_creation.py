import sys

if len(sys.argv) < 2:
    print("Usage: ft_ancient_text.py <file>")
    sys.exit()
print("=== Cyber Archives Recovery & Preservation ===")
print(f"Accessing file '{sys.argv[1]}'")
try:
    file = open(sys.argv[1])
    content = file.read()
    print(f"---\n{content}\n---")
    file.close()
    print(f"File '{sys.argv[1]}' closed.")
    lines = content.splitlines()
    transformed = "\n".join(line + "#" for line in lines)
    print("Transform data:")
    print(f"---\n{transformed}\n---")
    filename = input("Enter new file name (or empty): ")
    if not filename:
        print("Not saving data.")
    else:
        print(f"Saving data to '{filename}'")
        output_file = open(filename, "w")
        output_file.write(transformed)
        output_file.close()
        print(f"Data saved in file '{filename}'")
except PermissionError as error:
    print(f"Error opening file '{sys.argv[1]}': {error}")