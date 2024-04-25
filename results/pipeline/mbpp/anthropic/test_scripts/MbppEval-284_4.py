def check_element(list, element):
    all_equal = True
    for item in list:
        if item != element:
            all_equal = False
            break
    return all_equal

def check(candidate):
    assert check_element(["green", "orange", "black", "white"],'blue')==False
    assert check_element([1,2,3,4],7)==False
    assert check_element(["green", "green", "green", "green"],'green')==True

check(check_element)