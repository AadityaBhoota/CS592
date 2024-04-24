def find_substring(str_list, sub_str):
    for str_val in str_list:
        if sub_str in str_val:
            return True
    return False

# Test cases




def check(candidate):
    assert find_substring(["red", "black", "white", "green", "orange"],"ack")==True
    assert find_substring(["red", "black", "white", "green", "orange"],"abc")==False
    assert find_substring(["red", "black", "white", "green", "orange"],"ange")==True

check(find_substring)