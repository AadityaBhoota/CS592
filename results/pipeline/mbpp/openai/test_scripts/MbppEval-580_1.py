def even_ele(test_tuple, even_fnc):
    if not isinstance(test_tuple, tuple):
        raise TypeError("Input should be a tuple")
    
    def is_even(num):
        try:
            return even_fnc(num)
        except Exception as e:
            raise Exception("Error occurred while checking if the number is even: {}".format(e))

    def remove_odd_elements(tup):
        new_tuple = ()
        for elem in tup:
            if isinstance(elem, tuple):
                new_tuple += (remove_odd_elements(elem),)
            else:
                new_tuple += (elem,) if is_even(elem) else ()
        return new_tuple

    return remove_odd_elements(test_tuple)

def check(candidate):
    assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
    assert extract_even((5, 6, (8, 7, (4, 8)), 7, 9)) == (6, (8, (4, 8)))
    assert extract_even((5, 6, (9, 8, (4, 6)), 8, 10)) == (6, (8, (4, 6)), 8, 10)

check(even_ele)