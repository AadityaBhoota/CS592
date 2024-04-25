import math

def div_sum(n1, n2):
    """
    Determine if the sum of the divisors of two integers are the same.

    Parameters:
    n1 (int): The first integer.
    n2 (int): The second integer.

    Returns:
    bool: True if the sum of the divisors of n1 and n2 are the same, False otherwise.
    """
    def sum_divisors(n):
        """
        Calculate the sum of the divisors of a given integer.

        Parameters:
        n (int): The integer.

        Returns:
        int: The sum of the divisors of n.
        """
        divisors_sum = 1  # 1 is a divisor of every integer
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                divisors_sum += i
                if i != n // i:
                    divisors_sum += n // i
        return divisors_sum

    return sum_divisors(n1) == sum_divisors(n2)

def check(candidate):
    assert are_equivalent(36, 57) == False
    assert are_equivalent(2, 4) == False
    assert are_equivalent(23, 47) == True

check(div_sum)