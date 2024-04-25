def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def newman_prime(n):
    def helper(n, prime_candidate):
        count = 0
        while True:
            if is_prime(prime_candidate):
                count += 1
                if count == n:
                    return prime_candidate
            prime_candidate += 1

    return helper(n, 2)

# Test cases




def check(candidate):
    assert newman_prime(3) == 7
    assert newman_prime(4) == 17
    assert newman_prime(5) == 41

check(newman_prime)