def find_substring(str1, sub_str):
    found = False
    for s in str1:
        if sub_str in s:
            found = True
            break
    return found

def check(candidate):
    assert find_substring(["red", "black", "white", "green", "orange"],"ack")==True
    assert find_substring(["red", "black", "white", "green", "orange"],"abc")==False
    assert find_substring(["red", "black", "white", "green", "orange"],"ange")==True

check(find_substring)