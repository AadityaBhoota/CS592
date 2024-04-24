import math

def div_sum(n1, n2):
    """
    Determines if the sum of the divisors of two integers are the same.

    Args:
        n1 (int): The first integer.
        n2 (int): The second integer.

    Returns:
        bool: True if the sum of the divisors of n1 and n2 are the same, False otherwise.
    """
    def sum_of_divisors(n):
        """
        Calculates the sum of the divisors of an integer.

        Args:
            n (int): The integer.

        Returns:
            int: The sum of the divisors of n.
        """
        total = 0
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                total += i
                if i != n // i:
                    total += n // i
        return total

    return sum_of_divisors(n1) == sum_of_divisors(n2)

def check(candidate):
    assert are_equivalent(36, 57) == False
    assert are_equivalent(2, 4) == False
    assert are_equivalent(23, 47) == True

check(div_sum)