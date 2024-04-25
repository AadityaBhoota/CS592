def exchange(lst1, lst2):
    odd_count_lst1 = 0
    odd_count_lst2 = 0

    for num in lst1:
        if num % 2 != 0:
            odd_count_lst1 += 1

    for num in lst2:
        if num % 2 != 0:
            odd_count_lst2 += 1

    if (odd_count_lst1 + odd_count_lst2) % 2 == 0:
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