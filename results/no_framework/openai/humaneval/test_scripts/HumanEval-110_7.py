def exchange(lst1, lst2):
    # Check if all elements in lst1 are already even
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # Find the odd numbers in lst1 and even numbers in lst2
    odd_numbers = [num for num in lst1 if num % 2 != 0]
    even_numbers = [num for num in lst2 if num % 2 == 0]
    
    # Check if the number of odd numbers in lst1 is less than or equal to
    # the number of even numbers in lst2
    if len(odd_numbers) <= len(even_numbers):
        return "YES"
    else:
        return "NO"

# Test cases



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