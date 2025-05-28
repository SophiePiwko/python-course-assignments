import sys
import codecs

def rot13_file(filename):
    try:
        # Read the original content
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Apply ROT13 encoding
        rot13_content = codecs.encode(content, 'rot_13')

        # Write back the ROT13 encoded content
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(rot13_content)

        print(f"File '{filename}' has been encoded with ROT13.")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python rot13_file.py <filename>")
    else:
        rot13_file(sys.argv[1])