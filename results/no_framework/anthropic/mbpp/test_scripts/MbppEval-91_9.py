def find_substring(str_list, sub_str):
    """
    Checks if a string is present as a substring in a given list of string values.

    Args:
        str_list (list): A list of string values.
        sub_str (str): The substring to search for.

    Returns:
        bool: True if the substring is found, False otherwise.
    """
    for s in str_list:
        if sub_str in s:
            return True
    return False

def check(candidate):
    assert find_substring(["red", "black", "white", "green", "orange"],"ack")==True
    assert find_substring(["red", "black", "white", "green", "orange"],"abc")==False
    assert find_substring(["red", "black", "white", "green", "orange"],"ange")==True

check(find_substring)