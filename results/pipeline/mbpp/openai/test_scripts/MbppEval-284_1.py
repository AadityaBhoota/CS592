def check_element(lst, element):
    result = True
    for item in lst:
        if item != element:
            result = False
            break
    return result

def check(candidate):
    assert check_element(["green", "orange", "black", "white"],'blue')==False
    assert check_element([1,2,3,4],7)==False
    assert check_element(["green", "green", "green", "green"],'green')==True

check(check_element)