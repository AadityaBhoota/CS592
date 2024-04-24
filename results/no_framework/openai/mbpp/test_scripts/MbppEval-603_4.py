def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def get_ludic(n):
    primes = []
    for i in range(2, n+1):
        if is_prime(i):
            primes.append(i)

    ludic_numbers = [1]
    for prime in primes:
        next_number = ludic_numbers[-1] + prime
        if next_number <= n:
            ludic_numbers.append(next_number)

    return ludic_numbers

# Test cases




def check(candidate):
    assert get_ludic(10) == [1, 2, 3, 5, 7]
    assert get_ludic(25) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25]
    assert get_ludic(45) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25, 29, 37, 41, 43]

check(get_ludic)