def get_ludic(n):
    """
    Write a function to get all lucid numbers smaller than or equal to a given integer.

    Examples:
    get_ludic(10) == [1, 2, 3, 5, 7]
    get_ludic(25) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25]
    get_ludic(45) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25, 29, 37, 41, 43]
    """
    ludic_numbers = [1]
    i = 2
    while ludic_numbers[-1] <= n:
        next_ludic = ludic_numbers[-1] + i
        ludic_numbers.append(next_ludic)
        i += 1
    return ludic_numbers[:-1]

def check(candidate):
    assert get_ludic(10) == [1, 2, 3, 5, 7]
    assert get_ludic(25) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25]
    assert get_ludic(45) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25, 29, 37, 41, 43]

check(get_ludic)