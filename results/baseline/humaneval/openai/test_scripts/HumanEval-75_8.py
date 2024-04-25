def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_multiply_prime(a):
    if a < 6:  # Multiplication of 3 prime numbers starts from 2 * 3 * 5 = 30
        return False
    
    for i in range(2, a//2):
        if is_prime(i) and a % i == 0:
            remaining = a // i
            for j in range(i+1, remaining):
                if is_prime(j) and remaining % j == 0 and is_prime(remaining // j):
                    return True
    return False

# Test the function


def check(candidate):

    assert candidate(5) == False
    assert candidate(30) == True
    assert candidate(8) == True
    assert candidate(10) == False
    assert candidate(125) == True
    assert candidate(3 * 5 * 7) == True
    assert candidate(3 * 6 * 7) == False
    assert candidate(9 * 9 * 9) == False
    assert candidate(11 * 9 * 9) == False
    assert candidate(11 * 13 * 7) == True


check(is_multiply_prime)