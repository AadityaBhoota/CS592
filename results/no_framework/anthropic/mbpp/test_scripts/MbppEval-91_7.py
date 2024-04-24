def find_substring(str_list, sub_str):
    """
    Check if a given substring is present in any of the strings in the list.

    Args:
        str_list (list of str): The list of strings to search.
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