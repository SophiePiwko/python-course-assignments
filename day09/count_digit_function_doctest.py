# digit_counter.py
"""
Module for counting digit frequencies in numbers.

This module provides functions to analyze the frequency of digits (0-9) 
in collections of numbers. It includes both interactive and silent versions
for different use cases.
"""

def count_digits(numbers):
    """
    Count the frequency of each digit (0-9) in a list of numbers and print results.
    
    This function analyzes a list of numbers and counts how many times each digit
    (0 through 9) appears across all numbers. Results are printed to stdout and
    also returned as a dictionary.
    
    Args:
        numbers (list): List of integers to analyze
        
    Returns:
        dict: Dictionary with digits (0-9) as keys and their counts as values
        
    Examples:
        >>> result = count_digits([123, 456]) # doctest: +SKIP
        0 0
        1 1
        2 1
        3 1
        4 1
        5 1
        6 1
        7 0
        8 0
        9 0
        
        Note: This function prints output, so it's skipped in doctest.
        Use count_digits_silent() for testable examples.
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

def count_digits_silent(numbers):
    """
    Count the frequency of each digit (0-9) in a list of numbers without printing.
    
    This function analyzes a list of numbers and counts how many times each digit
    (0 through 9) appears across all numbers. Unlike count_digits(), this function
    does not print results, making it suitable for programmatic use and testing.
    
    Args:
        numbers (list): List of integers to analyze
        
    Returns:
        dict: Dictionary with digits (0-9) as keys and their counts as values
        
    Examples:
        >>> count_digits_silent([123])
        {0: 0, 1: 1, 2: 1, 3: 1, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        
        >>> count_digits_silent([111, 222])
        {0: 0, 1: 3, 2: 3, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        
        >>> count_digits_silent([1203, 1256, 312456, 98])
        {0: 1, 1: 3, 2: 3, 3: 2, 4: 1, 5: 2, 6: 2, 7: 0, 8: 1, 9: 1}
        
        >>> count_digits_silent([])
        {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        
        >>> count_digits_silent([0])
        {0: 1, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        
        >>> count_digits_silent([9876543210])
        {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}
    """
    count = [0] * 10 
    
    for num in numbers:
        for char in str(num):
            count[int(char)] += 1
    
    return {dig: count[dig] for dig in range(10)}

def get_most_common_digit(numbers):
    """
    Find the most frequently occurring digit in a list of numbers.
    
    Args:
        numbers (list): List of integers to analyze
        
    Returns:
        tuple: (digit, count) where digit is the most common digit and 
               count is how many times it appears. If there's a tie, 
               returns the smallest digit among the tied digits.
               
    Raises:
        ValueError: If the numbers list is empty
        
    Examples:
        >>> get_most_common_digit([111, 222])
        (1, 3)
        
        >>> get_most_common_digit([123, 321])
        (1, 2)
        
        >>> get_most_common_digit([987654321])
        (1, 1)
        
        >>> get_most_common_digit([1203, 1256, 312456, 98])
        (1, 3)
        
        >>> get_most_common_digit([])
        Traceback (most recent call last):
        ...
        ValueError: Cannot find most common digit in empty list
    """
    if not numbers:
        raise ValueError("Cannot find most common digit in empty list")
    
    digit_counts = count_digits_silent(numbers)
    max_count = max(digit_counts.values())
    
    # Return the smallest digit with the maximum count
    for digit in range(10):
        if digit_counts[digit] == max_count:
            return (digit, max_count)

def get_missing_digits(numbers):
    """
    Find digits (0-9) that do not appear in any of the given numbers.
    
    Args:
        numbers (list): List of integers to analyze
        
    Returns:
        list: Sorted list of digits that don't appear in the numbers
        
    Examples:
        >>> get_missing_digits([123, 456])
        [0, 7, 8, 9]
        
        >>> get_missing_digits([1234567890])
        []
        
        >>> get_missing_digits([111])
        [0, 2, 3, 4, 5, 6, 7, 8, 9]
        
        >>> get_missing_digits([])
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        >>> get_missing_digits([9876543210])
        []
    """
    digit_counts = count_digits_silent(numbers)
    return [digit for digit in range(10) if digit_counts[digit] == 0]

def analyze_digit_distribution(numbers):
    """
    Perform a complete analysis of digit distribution in a list of numbers.
    
    Args:
        numbers (list): List of integers to analyze
        
    Returns:
        dict: Analysis results containing:
            - 'counts': digit frequency dictionary
            - 'most_common': tuple of (digit, count) for most frequent digit
            - 'missing': list of digits that don't appear
            - 'total_digits': total number of digits analyzed
            
    Examples:
        >>> result = analyze_digit_distribution([123, 456])
        >>> result['counts'][1]
        1
        >>> result['most_common']
        (1, 1)
        >>> result['missing']
        [0, 7, 8, 9]
        >>> result['total_digits']
        6
        
        >>> result = analyze_digit_distribution([])
        >>> result['total_digits']
        0
        >>> len(result['missing'])
        10
    """
    if not numbers:
        return {
            'counts': {i: 0 for i in range(10)},
            'most_common': None,
            'missing': list(range(10)),
            'total_digits': 0
        }
    
    counts = count_digits_silent(numbers)
    most_common = get_most_common_digit(numbers)
    missing = get_missing_digits(numbers)
    total_digits = sum(counts.values())
    
    return {
        'counts': counts,
        'most_common': most_common,
        'missing': missing,
        'total_digits': total_digits
    }

if __name__ == "__main__":
    import doctest
    print("Running doctests...")
    result = doctest.testmod(verbose=True)
    print(f"\nDoctest Summary:")
    print(f"Tests run: {result.attempted}")
    print(f"Failures: {result.failed}")
    if result.failed == 0:
        print("All tests passed! ✓")
    else:
        print("Some tests failed! ✗")