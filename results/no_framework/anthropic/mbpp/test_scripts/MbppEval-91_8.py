def find_substring(str_list, sub_str):
    """
    Write a function to check if a string is present as a substring in a given list of string values.

    Examples:
    find_substring(["red", "black", "white", "green", "orange"], "ack") == True
    find_substring(["red", "black", "white", "green", "orange"], "abc") == False
    find_substring(["red", "black", "white", "green", "orange"], "ange") == True
    """
    for item in str_list:
        if sub_str in item:
            return True
    return False

def check(candidate):
    assert find_substring(["red", "black", "white", "green", "orange"],"ack")==True
    assert find_substring(["red", "black", "white", "green", "orange"],"abc")==False
    assert find_substring(["red", "black", "white", "green", "orange"],"ange")==True

check(find_substring)