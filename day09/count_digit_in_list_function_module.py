import sys
import os

sys.path.append('/C:/Course/Language/python-course-assignments/day09/digit_counter')

try:
    from digit_counter import count_digits, count_digits_silent
except ModuleNotFoundError:
    print("Error: Cannot find digit_counter module.")
    print("Make sure digit_counter.py is in the same directory as this script.")
    print(f"Current directory: {os.getcwd()}")
    print(f"Files in current directory: {os.listdir('.')}")
    sys.exit(1)

def main():
    # Original data
    numbers = [1203, 1256, 312456, 98]
    
    print("Digit frequency analysis:")
    print("-" * 25)
    digit_counts = count_digits(numbers)
    
    # Example of using the silent version
    print("\nUsing silent version for further processing:")
    silent_counts = count_digits_silent(numbers)
    
    # Find most common digit
    most_common_digit = max(silent_counts, key=silent_counts.get)
    print(f"Most common digit: {most_common_digit} (appears {silent_counts[most_common_digit]} times)")
    
    # Find digits that don't appear
    missing_digits = [digit for digit, count in silent_counts.items() if count == 0]
    if missing_digits:
        print(f"Digits not present: {missing_digits}")
    else:
        print("All digits (0-9) are present in the numbers")

if __name__ == "__main__":
    main()