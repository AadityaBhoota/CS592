def empty_list(length):
    """
    Write a function to create a list of N empty dictionaries.

    Examples:
    empty_list(5) == [{},{},{},{},{}]
    empty_list(6) == [{},{},{},{},{},{}]
    empty_list(7) == [{},{},{},{},{},{},{}]
    """
    return [{} for _ in range(length)]

def check(candidate):
    assert empty_list(5)==[{},{},{},{},{}]
    assert empty_list(6)==[{},{},{},{},{},{}]
    assert empty_list(7)==[{},{},{},{},{},{},{}]

check(empty_list)