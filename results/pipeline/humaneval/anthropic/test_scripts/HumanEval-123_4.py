def get_odd_collatz(n):
    """
    Given a positive integer n, return a sorted list that has the odd numbers in collatz sequence.
    """
    if n == 1:
        return [1]
    
    odd_numbers = []
    current_num = n
    
    while current_num != 1:
        if current_num % 2 == 1:
            odd_numbers.append(current_num)
        
        if current_num % 2 == 0:
            current_num //= 2
        else:
            current_num = 3 * current_num + 1
    
    return sorted(odd_numbers)

def check(candidate):

    # Check some simple cases
    assert candidate(14) == [1, 5, 7, 11, 13, 17]
    assert candidate(5) == [1, 5]
    assert candidate(12) == [1, 3, 5], "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert candidate(1) == [1], "This prints if this assert fails 2 (also good for debugging!)"


check(get_odd_collatz)