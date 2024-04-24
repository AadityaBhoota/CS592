def is_palindrome(num):
    return str(num) == str(num)[::-1]

def even_odd_palindrome(n):
    even_count = 0
    odd_count = 0

    for i in range(1, n+1):
        if is_palindrome(i):
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    
    return (even_count, odd_count)

# Test the function with example inputs



def check(candidate):

    # Check some simple cases
    assert candidate(123) == (8, 13)
    assert candidate(12) == (4, 6)
    assert candidate(3) == (1, 2)
    assert candidate(63) == (6, 8)
    assert candidate(25) == (5, 6)
    assert candidate(19) == (4, 6)
    assert candidate(9) == (4, 5), "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert candidate(1) == (0, 1), "This prints if this assert fails 2 (also good for debugging!)"


check(even_odd_palindrome)