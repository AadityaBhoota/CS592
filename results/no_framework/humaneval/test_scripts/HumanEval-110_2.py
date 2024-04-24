def exchange(lst1, lst2):
    # Check if all elements in lst1 are already even
    if all(num % 2 == 0 for num in lst1):
        return "YES"

    # Calculate the number of odd elements in lst1
    odd_count = sum(1 for num in lst1 if num % 2 != 0)

    # Calculate the number of odd elements in lst2
    odd_count += sum(1 for num in lst2 if num % 2 != 0)

    # If the total number of odd elements is even and greater than or equal to the length of lst1,
    # it is possible to exchange elements to make all elements of lst1 even
    if odd_count % 2 == 0 and odd_count >= len(lst1):
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