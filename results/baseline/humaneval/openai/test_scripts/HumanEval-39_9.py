def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def prime_fib(n: int):
    fib = [0, 1]
    while len(fib) <= n:
        fib.append(fib[-1] + fib[-2])
    i = 0
    while not is_prime(fib[i]):
        i += 1
    return fib[i]

# Testing the function








METADATA = {}


def check(candidate):
    assert candidate(1) == 2
    assert candidate(2) == 3
    assert candidate(3) == 5
    assert candidate(4) == 13
    assert candidate(5) == 89
    assert candidate(6) == 233
    assert candidate(7) == 1597
    assert candidate(8) == 28657
    assert candidate(9) == 514229
    assert candidate(10) == 433494437


check(prime_fib)