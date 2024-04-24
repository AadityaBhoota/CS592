def newman_prime(n): 
    if n == 0:
        return 1
    elif n == 1:
        return 2
    
    nsw_primes = [1, 2]
    i = 2
    while i < n:
        new_prime = 2 * nsw_primes[i-1] + nsw_primes[i-2]
        nsw_primes.append(new_prime)
        i += 1
    
    return nsw_primes[-1]

# Test cases




def check(candidate):
    assert newman_prime(3) == 7
    assert newman_prime(4) == 17
    assert newman_prime(5) == 41

check(newman_prime)