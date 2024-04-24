def get_ludic(n):
    """
    Get all Ludic numbers smaller than or equal to a given integer.

    Args:
        n (int): The upper bound for Ludic numbers.

    Returns:
        list: A list of all Ludic numbers less than or equal to `n`.
    """
    ludic = [True] * (n + 1)
    ludic[0] = ludic[1] = False
    primes = []

    for i in range(2, n + 1):
        if ludic[i]:
            primes.append(i)
            for j in range(i, n + 1, i):
                ludic[j] = False

    return [i for i in range(1, n + 1) if ludic[i]]

def check(candidate):
    assert get_ludic(10) == [1, 2, 3, 5, 7]
    assert get_ludic(25) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25]
    assert get_ludic(45) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25, 29, 37, 41, 43]

check(get_ludic)