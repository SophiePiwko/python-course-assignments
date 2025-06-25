def count_digits(numbers):
    """
    Count the frequency of each digit (0-9) in a list of numbers.
    
    Args:
        numbers (list): List of integers to analyze
        
    Returns:
        dict: Dictionary with digits as keys and their counts as values
    """
    count = [0] * 10 
    
    for num in numbers:
        for char in str(num):
            count[int(char)] += 1
    
    # Print results
    for dig in range(10):
        print(f"{dig} {count[dig]}")
    
    # Return counts as dictionary for potential reuse
    return {dig: count[dig] for dig in range(10)}

# Example usage:
if __name__ == "__main__":
    numbers = [1203, 1256, 312456, 98]
    digit_counts = count_digits(numbers)
    
    # You can also access the returned dictionary
    print(f"\nDigit 1 appears {digit_counts[1]} times")