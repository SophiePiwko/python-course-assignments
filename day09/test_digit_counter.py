# test_digit_counter.py
"""
Test suite for digit_counter module using pytest.

Run with: pytest test_digit_counter.py -v
"""

import pytest
from digit_counter import (count_digits_silent, get_most_common_digit, 
                          get_missing_digits, analyze_digit_distribution)


class TestCountDigitsSilent:
    """Test cases for count_digits_silent function."""
    
    def test_single_number(self):
        """Test with a single number."""
        result = count_digits_silent([123])
        expected = {0: 0, 1: 1, 2: 1, 3: 1, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        assert result == expected
    
    def test_multiple_numbers(self):
        """Test with multiple numbers."""
        result = count_digits_silent([111, 222])
        expected = {0: 0, 1: 3, 2: 3, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        assert result == expected
    
    def test_original_example(self):
        """Test with the original example data."""
        result = count_digits_silent([1203, 1256, 312456, 98])
        expected = {0: 1, 1: 3, 2: 3, 3: 2, 4: 1, 5: 2, 6: 2, 7: 0, 8: 1, 9: 1}
        assert result == expected
    
    def test_empty_list(self):
        """Test with empty list."""
        result = count_digits_silent([])
        expected = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        assert result == expected
    
    def test_single_zero(self):
        """Test with zero."""
        result = count_digits_silent([0])
        expected = {0: 1, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        assert result == expected
    
    def test_all_digits(self):
        """Test with a number containing all digits."""
        result = count_digits_silent([9876543210])
        expected = {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}
        assert result == expected
    
    def test_large_numbers(self):
        """Test with large numbers."""
        result = count_digits_silent([1000000, 2222222])
        expected = {0: 6, 1: 1, 2: 7, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        assert result == expected
    
    def test_return_type(self):
        """Test that function returns a dictionary."""
        result = count_digits_silent([123])
        assert isinstance(result, dict)
        assert len(result) == 10
        assert all(isinstance(k, int) for k in result.keys())
        assert all(isinstance(v, int) for v in result.values())


class TestGetMostCommonDigit:
    """Test cases for get_most_common_digit function."""
    
    def test_clear_winner(self):
        """Test when one digit is clearly most common."""
        result = get_most_common_digit([111, 222])
        assert result == (1, 3)
    
    def test_tie_returns_smallest(self):
        """Test that ties are broken by returning smallest digit."""
        result = get_most_common_digit([123, 321])
        assert result == (1, 2)  # 1, 2, 3 all appear twice, should return 1
    
    def test_single_digit_number(self):
        """Test with single digit numbers."""
        result = get_most_common_digit([7, 7, 7])
        assert result == (7, 3)
    
    def test_all_digits_equal(self):
        """Test when all digits appear equally."""
        result = get_most_common_digit([987654321])
        assert result == (1, 1)  # All appear once, should return smallest (1)
    
    def test_original_example(self):
        """Test with original example."""
        result = get_most_common_digit([1203, 1256, 312456, 98])
        assert result == (1, 3)
    
    def test_empty_list_raises_error(self):
        """Test that empty list raises ValueError."""
        with pytest.raises(ValueError, match="Cannot find most common digit in empty list"):
            get_most_common_digit([])
    
    def test_return_type(self):
        """Test return type is tuple with two integers."""
        result = get_most_common_digit([123])
        assert isinstance(result, tuple)
        assert len(result) == 2
        assert isinstance(result[0], int)
        assert isinstance(result[1], int)
        assert 0 <= result[0] <= 9
        assert result[1] > 0


class TestGetMissingDigits:
    """Test cases for get_missing_digits function."""
    
    def test_some_missing(self):
        """Test with some digits missing."""
        result = get_missing_digits([123, 456])
        assert result == [0, 7, 8, 9]
    
    def test_no_missing(self):
        """Test when no digits are missing."""
        result = get_missing_digits([1234567890])
        assert result == []
    
    def test_most_missing(self):
        """Test when most digits are missing."""
        result = get_missing_digits([111])
        assert result == [0, 2, 3, 4, 5, 6, 7, 8, 9]
    
    def test_empty_list(self):
        """Test with empty list (all digits missing)."""
        result = get_missing_digits([])
        assert result == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    def test_all_digits_present(self):
        """Test with all digits present multiple times."""
        result = get_missing_digits([9876543210, 1234567890])
        assert result == []
    
    def test_return_type_and_sorted(self):
        """Test return type is sorted list."""
        result = get_missing_digits([987, 321])
        assert isinstance(result, list)
        assert all(isinstance(x, int) for x in result)
        assert result == sorted(result)  # Should be sorted
        assert all(0 <= x <= 9 for x in result)  # All should be single digits


class TestAnalyzeDigitDistribution:
    """Test cases for analyze_digit_distribution function."""
    
    def test_normal_case(self):
        """Test with normal input."""
        result = analyze_digit_distribution([123, 456])
        
        assert 'counts' in result
        assert 'most_common' in result
        assert 'missing' in result
        assert 'total_digits' in result
        
        assert result['counts'][1] == 1
        assert result['most_common'] == (1, 1)  # All digits appear once, returns smallest
        assert result['missing'] == [0, 7, 8, 9]
        assert result['total_digits'] == 6
    
    def test_empty_list(self):
        """Test with empty list."""
        result = analyze_digit_distribution([])
        
        assert result['counts'] == {i: 0 for i in range(10)}
        assert result['most_common'] is None
        assert result['missing'] == list(range(10))
        assert result['total_digits'] == 0
    
    def test_comprehensive_analysis(self):
        """Test comprehensive analysis with original data."""
        result = analyze_digit_distribution([1203, 1256, 312456, 98])
        
        assert result['counts'][1] == 3  # Digit 1 appears 3 times
        assert result['most_common'] == (1, 3)
        assert 7 in result['missing']  # Digit 7 doesn't appear
        assert result['total_digits'] == 16  # Total digits in all numbers
    
    def test_return_structure(self):
        """Test the structure of returned dictionary."""
        result = analyze_digit_distribution([123])
        
        # Check all required keys exist
        required_keys = ['counts', 'most_common', 'missing', 'total_digits']
        assert all(key in result for key in required_keys)
        
        # Check types
        assert isinstance(result['counts'], dict)
        assert isinstance(result['most_common'], tuple) or result['most_common'] is None
        assert isinstance(result['missing'], list)
        assert isinstance(result['total_digits'], int)
        
        # Check counts dictionary structure
        assert len(result['counts']) == 10
        assert all(isinstance(k, int) and 0 <= k <= 9 for k in result['counts'].keys())
        assert all(isinstance(v, int) and v >= 0 for v in result['counts'].values())


class TestEdgeCases:
    """Test edge cases and error conditions."""
    
    def test_negative_numbers(self):
        """Test with negative numbers (should work with absolute values)."""
        # Note: The current implementation converts to string, so -123 becomes "-123"
        # This will count the digits 1, 2, 3 (ignoring the minus sign)
        result = count_digits_silent([-123])
        assert result[1] == 1
        assert result[2] == 1  
        assert result[3] == 1
    
    def test_zero_variations(self):
        """Test with various zero representations."""
        result = count_digits_silent([0, 00, 000])
        assert result[0] == 3  # Three zeros
    
    def test_very_large_numbers(self):
        """Test with very large numbers."""
        large_num = 12345678901234567890
        result = count_digits_silent([large_num])
        # This number has two of each digit 0-9
        for digit in range(10):
            assert result[digit] == 2
    
    def test_single_digit_analysis(self):
        """Test analysis with single digit numbers."""
        result = analyze_digit_distribution([5])
        assert result['most_common'] == (5, 1)
        assert len(result['missing']) == 9
        assert result['total_digits'] == 1


class TestIntegration:
    """Integration tests combining multiple functions."""
    
    def test_consistency_between_functions(self):
        """Test that different functions give consistent results."""
        numbers = [1203, 1256, 312456, 98]
        
        # Get results from different functions
        silent_counts = count_digits_silent(numbers)
        most_common = get_most_common_digit(numbers)
        missing = get_missing_digits(numbers)
        analysis = analyze_digit_distribution(numbers)
        
        # Check consistency
        assert analysis['counts'] == silent_counts
        assert analysis['most_common'] == most_common
        assert analysis['missing'] == missing
        
        # Verify most common digit count matches
        digit, count = most_common
        assert silent_counts[digit] == count
        
        # Verify missing digits have zero count
        for digit in missing:
            assert silent_counts[digit] == 0
    
    def test_total_digits_calculation(self):
        """Test that total digits calculation is correct."""
        numbers = [123, 4567]
        analysis = analyze_digit_distribution(numbers)
        
        # Manual calculation: 123 has 3 digits, 4567 has 4 digits = 7 total
        expected_total = len('123') + len('4567')
        assert analysis['total_digits'] == expected_total
        
        # Also verify sum of all counts equals total
        assert sum(analysis['counts'].values()) == analysis['total_digits']


# Pytest fixtures for common test data
@pytest.fixture
def original_data():
    """Fixture providing the original test data."""
    return [1203, 1256, 312456, 98]

@pytest.fixture
def empty_data():
    """Fixture providing empty data."""
    return []

@pytest.fixture
def simple_data():
    """Fixture providing simple test data."""
    return [123, 456]


# Parametrized tests
@pytest.mark.parametrize("numbers,expected_most_common", [
    ([111], (1, 3)),
    ([222, 333], (2, 3)),
    ([123, 321], (1, 2)),  # Tie broken by smallest digit
    ([9876543210], (0, 1)),  # All equal, returns smallest
])
def test_most_common_digit_parametrized(numbers, expected_most_common):
    """Parametrized test for most common digit scenarios."""
    result = get_most_common_digit(numbers)
    assert result == expected_most_common


@pytest.mark.parametrize("numbers,expected_missing_count", [
    ([123], 7),  # Missing: 0,4,5,6,7,8,9
    ([1234567890], 0),  # No missing digits
    ([], 10),  # All digits missing
    ([111], 9),  # Missing: 0,2,3,4,5,6,7,8,9
])
def test_missing_digits_count_parametrized(numbers, expected_missing_count):
    """Parametrized test for missing digits count."""
    result = get_missing_digits(numbers)
    assert len(result) == expected_missing_count


if __name__ == "__main__":
    # Run pytest programmatically if script is executed directly
    import subprocess
    import sys
    
    print("Running pytest...")
    result = subprocess.run([sys.executable, "-m", "pytest", __file__, "-v"], 
                          capture_output=True, text=True)
    
    print(result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)
    
    sys.exit(result.returncode)