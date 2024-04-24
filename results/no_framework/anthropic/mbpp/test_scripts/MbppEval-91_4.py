def find_substring(str_list, sub_str):
    """
    Check if a substring is present in a given list of strings.

    Args:
        str_list (list of str): A list of string values.
        sub_str (str): The substring to search for.

    Returns:
        bool: True if the substring is found, False otherwise.
    """
    for string in str_list:
        if sub_str in string:
            return True
    return False

def check(candidate):
    assert find_substring(["red", "black", "white", "green", "orange"],"ack")==True
    assert find_substring(["red", "black", "white", "green", "orange"],"abc")==False
    assert find_substring(["red", "black", "white", "green", "orange"],"ange")==True

check(find_substring)