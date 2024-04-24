def exchange(lst1, lst2):
    # Check if all elements in lst1 are already even
    if all(num % 2 == 0 for num in lst1):
        return "YES"

    # Calculate the count of even numbers in lst1
    even_count = sum(1 for num in lst1 if num % 2 == 0)

    # Calculate the total count of even and odd numbers in both lists
    total_even = even_count + sum(1 for num in lst2 if num % 2 == 0)
    total_odd = len(lst1) + len(lst2) - total_even

    # Check if there are enough even numbers in both lists to make all elements in lst1 even
    if total_even >= len(lst1) or (total_even > even_count and total_odd % 2 == 0):
        return "YES"
    else:
        return "NO"

# Test cases
print(exchange([1, 2, 3, 4], [1, 2, 3, 4]))  # Output: "YES"
print(exchange([1, 2, 3, 4], [1, 5, 3, 4]))  # Output: "NO"

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