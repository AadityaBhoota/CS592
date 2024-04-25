def newman_prime(n):
    '''
    Write a function to find the nth newman–shanks–williams prime number.

    Examples:
    newman_prime(3) == 7
    newman_prime(4) == 17
    newman_prime(5) == 41
    '''

    def calculate_nswn(x):
        if x == 0:
            return 1
        if x == 1:
            return 2
        return 2 * calculate_nswn(x - 1) - calculate_nswn(x - 2)

    return calculate_nswn(n)

def check(candidate):
    assert newman_prime(3) == 7
    assert newman_prime(4) == 17
    assert newman_prime(5) == 41

check(newman_prime)