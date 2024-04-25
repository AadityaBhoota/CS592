def check_value(dict_data, n):
    """
    Write a function to check if all values are the same in a dictionary.

    Examples:
    check_value({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}, 10) == False
    check_value({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}, 12) == True
    check_value({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}, 5) == False
    """
    return len(set(dict_data.values())) == 1 and list(dict_data.values())[0] == n

def check(candidate):
    assert check_value({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12},10)==False
    assert check_value({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12},12)==True
    assert check_value({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12},5)==False

check(check_value)