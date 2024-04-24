def check_element(lst, element):
    return all(item == element for item in lst)

# Test cases




def check(candidate):
    assert check_element(["green", "orange", "black", "white"],'blue')==False
    assert check_element([1,2,3,4],7)==False
    assert check_element(["green", "green", "green", "green"],'green')==True

check(check_element)