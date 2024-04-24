def digitSum(s):
    total_sum = 0
    for char in s:
        if char.isupper():
            total_sum += ord(char)
    return total_sum

# Test the function with the provided examples
print(digitSum(""))        # Output: 0
print(digitSum("abAB"))    # Output: 131
print(digitSum("abcCd"))   # Output: 67
print(digitSum("helloE"))  # Output: 69
print(digitSum("woArBld")) # Output: 131
print(digitSum("aAaaaXa")) # Output: 153

def check(candidate):

    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate("") == 0, "Error"
    assert candidate("abAB") == 131, "Error"
    assert candidate("abcCd") == 67, "Error"
    assert candidate("helloE") == 69, "Error"
    assert candidate("woArBld") == 131, "Error"
    assert candidate("aAaaaXa") == 153, "Error"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate(" How are yOu?") == 151, "Error"
    assert candidate("You arE Very Smart") == 327, "Error"


check(digitSum)