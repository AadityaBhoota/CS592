def exchange(lst1, lst2):
    # Count the number of odd elements in lst1
    odd_count = sum(1 for num in lst1 if num % 2 != 0)
    
    # If there are odd elements in lst1, check if there are enough even elements in lst2 to exchange
    if odd_count > 0:
        even_count = sum(1 for num in lst2 if num % 2 == 0)
        return "YES" if even_count >= odd_count else "NO"
    
    return "YES"  # If lst1 already has no odd elements, return "YES"

# Test cases
print(exchange([1, 2, 3, 4], [1, 2, 3, 4]))  # Output should be "YES"
print(exchange([1, 2, 3, 4], [1, 5, 3, 4]))  # Output should be "NO"

def check(candidate):

    # Check some simple cases
    assert candidate([1, 2, 3, 4], [1, 2, 3, 4]) == "YES"
    assert candidate([1, 2, 3, 4], [1, 5, 3, 4]) == "NO"
    assert candidate([1, 2, 3, 4], [2, 1, 4, 3]) == "YES" 
    assert candidate([5, 7, 3], [2, 6, 4]) == "YES"
    assert candidate([5, 7, 3], [2, 6, 3]) == "NO" 
    assert candidate([3, 2, 6, 1, 8, 9], [3, 5, 5, 1, 1, 1]) == "NO"

    # Check some edge cases that are easy to work out by hand.
    assert candidate([100, 200], [200, 200]) == "YES"


check(exchange)