import sys

def load_colors(filename):
    try:
        with open(filename, 'r') as f:
            # Read lines, strip whitespace, ignore empty lines
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file '{filename}': {e}")
        sys.exit(1)

def print_menu(colors):
    print("Select a color:")
    for idx, color in enumerate(colors, start=1):
        print(f"{idx}. {color}")

def process_input(user_input, colors):
    user_input = user_input.strip()
    if user_input.isdigit():
        num = int(user_input)
        if 1 <= num <= len(colors):
            return colors[num - 1]
        else:
            print(f"Number {num} is out of range.")
            return None
    else:
        user_input_lower = user_input.lower()
        # Find matching color ignoring case
        for i, color in enumerate(colors):
            if color.lower() == user_input_lower:
                return str(i + 1)
        print(f"Color '{user_input}' is not in the list.")
        return None

def get_user_choice(colors):
    while True:
        user_input = input("Enter the number or name of your choice: ")
        result = process_input(user_input, colors)
        if result is not None:
            return result
        print("Please try again.")

def main():
    if len(sys.argv) < 2:
        print("No command line argument was given.")
        sys.exit(1)
        
    color_file = sys.argv[1]
    colors = load_colors(color_file)

    # Optional second argument: number or color name
    if len(sys.argv) == 3:
        arg = sys.argv[2]
        result = process_input(arg, colors)
        if result is not None:
            print(f"You selected: {result}")
            return
        else:
            print("Falling back to interactive mode.\n")

    print_menu(colors)
    selected = get_user_choice(colors)
    print(f"You selected: {selected}")

if __name__ == "__main__":
    main()
