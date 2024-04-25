def sum(a, b):
    """
    Find the sum of common divisors of two given numbers.

    Examples:
    sum(10, 15) == 6
    sum(100, 150) == 93
    sum(4, 6) == 3
    """
    def find_divisors(n):
        """
        Helper function to find all the divisors of a given number.
        """
        divisors = []
        for i in range(1, n+1):
            if n % i == 0:
                divisors.append(i)
        return divisors

    a_divisors = find_divisors(a)
    b_divisors = find_divisors(b)
    common_divisors = set(a_divisors) & set(b_divisors)
    return sum(common_divisors)

def check(candidate):
    assert sum(10,15) == 6
    assert sum(100,150) == 93
    assert sum(4,6) == 3

check(sum)