def get_ludic(n):
    """
    Write a function to get all ludic numbers smaller than or equal to a given integer.

    Examples:
    get_ludic(10) == [1, 2, 3, 5, 7]
    get_ludic(25) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25]
    get_ludic(45) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25, 29, 37, 41, 43]
    """
    ludic = [True] * (n + 1)
    ludic[0] = False
    i = 1
    while i * (i + 1) <= n:
        if ludic[i]:
            j = i + 1
            while j <= n:
                ludic[j] = False
                j += i + 1
        i += 1
    return [i for i in range(1, n + 1) if ludic[i]]

def check(candidate):
    assert get_ludic(10) == [1, 2, 3, 5, 7]
    assert get_ludic(25) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25]
    assert get_ludic(45) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25, 29, 37, 41, 43]

check(get_ludic)