def count_Primes_nums(n):
    count = 0
    for num in range(2, n):
        if is_prime(num):
            count += 1
    return count

def check(candidate):
    assert count_Primes_nums(5) == 2
    assert count_Primes_nums(10) == 4
    assert count_Primes_nums(100) == 25

check(count_Primes_nums)