import sys

def count_digits_in_file(filename):
    digit_counts = {str(d): 0 for d in range(10)}

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                for char in line:
                    if char.isdigit():
                        digit_counts[char] += 1
        
        # Write results to report.txt
        with open('report.txt', 'w', encoding='utf-8') as report_file:
            for digit in sorted(digit_counts.keys()):
                report_file.write(f"{digit}: {digit_counts[digit]}\n")

        print("Digit counts saved to report.txt")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python count_digits_in_file.py <filename>")
    else:
        count_digits_in_file(sys.argv[1])
