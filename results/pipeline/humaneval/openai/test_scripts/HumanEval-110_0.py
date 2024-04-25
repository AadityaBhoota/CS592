def exchange(lst1, lst2):
    if not lst1 or not lst2:
        return "NO"
    
    for num in lst1:
        if num % 2 != 0:
            for num2 in lst2:
                if num2 % 2 == 0:
                    lst1[lst1.index(num)], lst2[lst2.index(num2)] = num2, num
                    break
    
    if all(num % 2 == 0 for num in lst1):
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