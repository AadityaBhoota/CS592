def get_ludic(n):
    """
    Return all Ludic numbers less than or equal to the given integer n.
    
    Ludic numbers are defined as the numbers that are not divisible by 2, 3, 5, 7, 11, 13, 17, ...
    """
    ludic_numbers = [1]
    i = 2
    while ludic_numbers[-1] <= n:
        is_ludic = True
        for p in ludic_numbers:
            if i % p == 0:
                is_ludic = False
                break
        if is_ludic:
            ludic_numbers.append(i)
        i += 1
    return ludic_numbers[:-1]

def check(candidate):
    assert get_ludic(10) == [1, 2, 3, 5, 7]
    assert get_ludic(25) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25]
    assert get_ludic(45) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25, 29, 37, 41, 43]

check(get_ludic)