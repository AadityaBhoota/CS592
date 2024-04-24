def number_of_substrings(input_str):
    length = len(input_str)
    return int(length*(length+1)/2)

# Test the function with examples




def check(candidate):
    assert number_of_substrings("abc") == 6
    assert number_of_substrings("abcd") == 10
    assert number_of_substrings("abcde") == 15

check(number_of_substrings)