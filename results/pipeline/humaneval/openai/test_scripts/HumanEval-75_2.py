from itertools import combinations

def is_multiply_prime(a):
    if a >= 100:
        return False

    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

    prime_factors = [i for i in range(2, a) if is_prime(i) and a % i == 0]

    for combo in combinations(prime_factors, 3):
        if combo[0] * combo[1] * combo[2] == a:
            return True

    return False

def check(candidate):

    assert candidate(5) == False
    assert candidate(30) == True
    assert candidate(8) == True
    assert candidate(10) == False
    assert candidate(125) == True
    assert candidate(3 * 5 * 7) == True
    assert candidate(3 * 6 * 7) == False
    assert candidate(9 * 9 * 9) == False
    assert candidate(11 * 9 * 9) == False
    assert candidate(11 * 13 * 7) == True


check(is_multiply_prime)