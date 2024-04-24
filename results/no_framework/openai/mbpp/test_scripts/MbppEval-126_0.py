def sum_of_common_divisors(a, b):
    def get_divisors(n):
        divisors = [1]
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
        return divisors

    divisors_a = get_divisors(a)
    divisors_b = get_divisors(b)

    common_divisors = set(divisors_a).intersection(set(divisors_b))

    return sum(common_divisors)

# Test cases




def check(candidate):
    assert sum(10,15) == 6
    assert sum(100,150) == 93
    assert sum(4,6) == 3

check(sum)