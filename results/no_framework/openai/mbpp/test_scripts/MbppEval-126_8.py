def sum(a, b):
    def find_divisors(n):
        divisors = []
        for i in range(1, n+1):
            if n % i == 0:
                divisors.append(i)
        return divisors

    divisors_a = find_divisors(a)
    divisors_b = find_divisors(b)

    common_divisors = set(divisors_a) & set(divisors_b)

    return sum(common_divisors)

# Test Cases




def check(candidate):
    assert sum(10,15) == 6
    assert sum(100,150) == 93
    assert sum(4,6) == 3

check(sum)