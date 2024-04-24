def new_tuple(test_list, test_str):
    """
    Write a function to create a new tuple from the given string and list.

    Examples:
    new_tuple(["WEB", "is"], "best") == ('WEB', 'is', 'best')
    new_tuple(["We", "are"], "Developers") == ('We', 'are', 'Developers')
    new_tuple(["Part", "is"], "Wrong") == ('Part', 'is', 'Wrong')
    """
    return tuple([*test_list, test_str])

def check(candidate):
    assert new_tuple(["WEB", "is"], "best") == ('WEB', 'is', 'best')
    assert new_tuple(["We", "are"], "Developers") == ('We', 'are', 'Developers')
    assert new_tuple(["Part", "is"], "Wrong") == ('Part', 'is', 'Wrong')

check(new_tuple)