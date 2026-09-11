import sys

if len(sys.argv) < 2:
    print("Usage: ft_ancient_text.py <file>")
    sys.exit()
print("=== Cyber Archives Recovery ===")
print(f"Accessing file '{sys.argv[1]}'")
try:
    file = open(sys.argv[1])
    content = file.read()
    print(f"---\n{content} \n---")
    file.close()
    print(f"File '{sys.argv[1]}' closed.")
except FileNotFoundError as error:
    print(f"Error opening file '{sys.argv[1]}': {error}")
except PermissionError as error:
    print(f"Error opening file '{sys.argv[1]}': {error}")