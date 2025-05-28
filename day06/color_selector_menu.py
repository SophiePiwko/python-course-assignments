import sys

colors = ['blue', 'green', 'yellow', 'white']

def print_menu():
    print("Select a color:")
    for idx, color in enumerate(colors, start=1):
        print(f"{idx}. {color}")

def process_input(user_input):
    user_input = user_input.strip()
    if user_input.isdigit():
        num = int(user_input)
        if 1 <= num <= len(colors):
            # Input is number, output color name
            return colors[num - 1]
        else:
            print(f"Number {num} is out of range.")
            return None
    else:
        user_input_lower = user_input.lower()
        if user_input_lower in colors:
            # Input is color name, output number as string
            return str(colors.index(user_input_lower) + 1)
        else:
            print(f"Color '{user_input}' is not in the list.")
            return None

def get_user_choice():
    while True:
        user_input = input("Enter the number or name of your choice: ")
        result = process_input(user_input)
        if result is not None:
            return result
        print("Please try again.")

def main():
    if len(sys.argv) == 2:
        result = process_input(sys.argv[1])
        if result is not None:
            print(f"You selected: {result}")
            return
        else:
            print("Falling back to interactive mode.\n")

    print_menu()
    selected = get_user_choice()
    print(f"You selected: {selected}")

if __name__ == "__main__":
    main()
