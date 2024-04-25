def exchange(lst1, lst2):
    if all(x % 2 == 0 for x in lst1):
        return "YES"  # No exchange needed

    odd_count_lst1 = sum(1 for x in lst1 if x % 2 != 0)
    odd_count_total = odd_count_lst1 + sum(1 for x in lst2 if x % 2 != 0)

    if odd_count_total >= odd_count_lst1:
        return "YES"  # There are enough odd elements in lst2 to exchange with lst1
    else:
        return "NO"  # Not enough odd elements in lst2 for the exchange

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