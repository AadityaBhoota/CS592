def check_value(d, n):
    """
    Write a function to check if all values are the same in a dictionary.

    Examples:
    check_value({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12},10) == False
    check_value({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12},12) == True
    check_value({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12},5) == False
    """
    return len(set(d.values())) == 1 and n in d.values()

def check(candidate):
    assert check_value({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12},10)==False
    assert check_value({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12},12)==True
    assert check_value({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12},5)==False

check(check_value)