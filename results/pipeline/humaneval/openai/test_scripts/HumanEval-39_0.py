def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_fib(n: int) -> int:
    def generate_fibonacci():
        a, b = 0, 1
        yield a
        yield b
        while True:
            a, b = b, a + b
            yield b

    fibonacci_gen = generate_fibonacci()
    count = 0
    while count < n:
        fib_num = next(fibonacci_gen)
        if is_prime(fib_num):
            count += 1

    return fib_num



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