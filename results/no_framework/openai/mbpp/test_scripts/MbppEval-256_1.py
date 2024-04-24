def count_Primes_nums(n):
    if n < 2:
        return 0
    
    primes = [True] * n
    primes[0] = primes[1] = False
    
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            primes[i*i:n:i] = [False] * len(primes[i*i:n:i])
    
    return sum(primes)

# Test cases




def check(candidate):
    assert count_Primes_nums(5) == 2
    assert count_Primes_nums(10) == 4
    assert count_Primes_nums(100) == 25

check(count_Primes_nums)