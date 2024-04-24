def newman_prime(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    ns_numbers = [1, 1]
    primes = []
    num = 3

    while len(primes) < n:
        next_num = 2 * ns_numbers[num-1] + ns_numbers[num-2]
        ns_numbers.append(next_num)
        if is_prime(next_num):
            primes.append(next_num)
        num += 1

    return primes[n - 1]

# Test cases




def check(candidate):
    assert newman_prime(3) == 7
    assert newman_prime(4) == 17
    assert newman_prime(5) == 41

check(newman_prime)