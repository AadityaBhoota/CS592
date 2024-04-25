def new_tuple(test_list, test_str):
    new_tuple = tuple(test_list) + (test_str,)
    return new_tuple

def check(candidate):
    assert new_tuple(["WEB", "is"], "best") == ('WEB', 'is', 'best')
    assert new_tuple(["We", "are"], "Developers") == ('We', 'are', 'Developers')
    assert new_tuple(["Part", "is"], "Wrong") == ('Part', 'is', 'Wrong')

check(new_tuple)