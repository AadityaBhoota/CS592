def words_string(s):
    # Split the input string by commas or spaces
    words = [word.strip() for word in s.replace(",", " ").split()]

    return words

# Test cases
print(words_string("Hi, my name is John"))  # Output: ["Hi", "my", "name", "is", "John"]
print(words_string("One, two, three, four, five, six"))  # Output: ["One", "two", "three", "four", "five", "six"]

def check(candidate):

    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    assert candidate("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    assert candidate("Hi, my name") == ["Hi", "my", "name"]
    assert candidate("One,, two, three, four, five, six,") == ["One", "two", "three", "four", "five", "six"]

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate("") == []
    assert candidate("ahmed     , gamal") == ["ahmed", "gamal"]


check(words_string)