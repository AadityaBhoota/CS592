def get_ludic(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    p = 2
    while p ** 2 <= n:
        if primes[p] == True:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    lucid_numbers = []
    for num in range(2, n + 1):
        if primes[num] or num % 2 == 0:
            lucid_numbers.append(num)

    return lucid_numbers

# Test cases




def check(candidate):
    assert get_ludic(10) == [1, 2, 3, 5, 7]
    assert get_ludic(25) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25]
    assert get_ludic(45) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25, 29, 37, 41, 43]

check(get_ludic)