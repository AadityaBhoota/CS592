def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    
    # Step 0: Check if the input n is a positive integer
    if not isinstance(n, int) or n <= 0:
        return "Input must be a positive integer."
    
    count = 0
    
    # Step 2: Iterate through all n-digit positive integers
    for i in range(10**(n-1), 10**n):
        if str(i)[0] == '1' or str(i)[-1] == '1':
            count += 1

    return count

def check(candidate):

    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate(1) == 1
    assert candidate(2) == 18
    assert candidate(3) == 180
    assert candidate(4) == 1800
    assert candidate(5) == 18000

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"


check(starts_one_ends)