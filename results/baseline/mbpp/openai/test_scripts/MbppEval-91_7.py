def find_substring(string_list, sub_str):
    for string in string_list:
        if sub_str in string:
            return True
    return False

# Test cases




def check(candidate):
    assert find_substring(["red", "black", "white", "green", "orange"],"ack")==True
    assert find_substring(["red", "black", "white", "green", "orange"],"abc")==False
    assert find_substring(["red", "black", "white", "green", "orange"],"ange")==True

check(find_substring)