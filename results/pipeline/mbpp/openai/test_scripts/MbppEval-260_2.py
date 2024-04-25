def newman_prime(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def generate_prime_numbers(n):
        prime_numbers = []
        num = 2
        
        while len(prime_numbers) < n:
            if is_prime(num):
                prime_numbers.append(num)
            num += 1
            
        return prime_numbers

    def newman_shanks_williams_prime(k, previous_nsw_primes):
        if k == 0:
            return 1
        elif k == 1:
            return 1
        else:
            return 2**k * previous_nsw_primes[k-1] - previous_nsw_primes[k-2] + 1

    prime_numbers = generate_prime_numbers(n)
    nsw_primes = [newman_shanks_williams_prime(k, nsw_primes) for k, nsw_primes in enumerate([1] + prime_numbers)]
    
    return nsw_primes[n-1]

def check(candidate):
    assert newman_prime(3) == 7
    assert newman_prime(4) == 17
    assert newman_prime(5) == 41

check(newman_prime)