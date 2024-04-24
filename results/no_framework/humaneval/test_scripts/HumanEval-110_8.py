def exchange(lst1, lst2):
    # Check if all elements in lst1 are already even
    if all(num % 2 == 0 for num in lst1):
        return "YES"

    # Find the smallest odd number in lst1 and the smallest even number in lst2
    min_odd = min(num for num in lst1 if num % 2 != 0)
    min_even = min(num for num in lst2 if num % 2 == 0)

    # Check if the smallest odd number in lst1 is greater than the smallest even number in lst2
    if min_odd > min_even:
        return "YES"
    else:
        return "NO"

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