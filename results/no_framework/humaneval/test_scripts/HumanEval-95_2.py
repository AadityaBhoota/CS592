def check_dict_case(d):
    if not d:
        return False

    lower_keys = all(isinstance(key, str) and key.islower() for key in d.keys())
    upper_keys = all(isinstance(key, str) and key.isupper() for key in d.keys())

    return lower_keys or upper_keys

# Test cases
print(check_dict_case({"a": "apple", "b": "banana"}))  # True
print(check_dict_case({"a": "apple", "A": "banana", "B": "banana"}))  # False
print(check_dict_case({"a": "apple", 8: "banana", "a": "apple"}))  # False
print(check_dict_case({"Name": "John", "Age": "36", "City": "Houston"}))  # False
print(check_dict_case({"STATE": "NC", "ZIP": "12345"}))  # True

def check(candidate):

    # Check some simple cases
    assert candidate({"p":"pineapple", "b":"banana"}) == True, "First test error: " + str(candidate({"p":"pineapple", "b":"banana"}))
    assert candidate({"p":"pineapple", "A":"banana", "B":"banana"}) == False, "Second test error: " + str(candidate({"p":"pineapple", "A":"banana", "B":"banana"}))
    assert candidate({"p":"pineapple", 5:"banana", "a":"apple"}) == False, "Third test error: " + str(candidate({"p":"pineapple", 5:"banana", "a":"apple"}))
    assert candidate({"Name":"John", "Age":"36", "City":"Houston"}) == False, "Fourth test error: " + str(candidate({"Name":"John", "Age":"36", "City":"Houston"}))
    assert candidate({"STATE":"NC", "ZIP":"12345" }) == True, "Fifth test error: " + str(candidate({"STATE":"NC", "ZIP":"12345" }))      
    assert candidate({"fruit":"Orange", "taste":"Sweet" }) == True, "Fourth test error: " + str(candidate({"fruit":"Orange", "taste":"Sweet" }))      


    # Check some edge cases that are easy to work out by hand.
    assert candidate({}) == False, "1st edge test error: " + str(candidate({}))


check(check_dict_case)