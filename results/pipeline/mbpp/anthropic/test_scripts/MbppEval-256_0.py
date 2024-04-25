def count_Primes_nums(n):
    if n < 2:
        return 0
    
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n+1, i):
                is_prime[j] = False
    
    return sum(is_prime)

def check(candidate):
    assert count_Primes_nums(5) == 2
    assert count_Primes_nums(10) == 4
    assert count_Primes_nums(100) == 25

check(count_Primes_nums)