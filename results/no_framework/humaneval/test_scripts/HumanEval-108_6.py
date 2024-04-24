def count_nums(arr):
    def sum_digits(num):
        return sum([int(d) for d in str(abs(num))])

    count = 0
    for num in arr:
        if sum_digits(num) > 0:
            count += 1
    return count

# Test cases
print(count_nums([]))        # Output should be 0
print(count_nums([-1, 11, -11]))  # Output should be 1
print(count_nums([1, 1, 2]))       # Output should be 3

def check(candidate):

    # Check some simple cases
    assert candidate([]) == 0
    assert candidate([-1, -2, 0]) == 0
    assert candidate([1, 1, 2, -2, 3, 4, 5]) == 6
    assert candidate([1, 6, 9, -6, 0, 1, 5]) == 5
    assert candidate([1, 100, 98, -7, 1, -1]) == 4
    assert candidate([12, 23, 34, -45, -56, 0]) == 5
    assert candidate([-0, 1**0]) == 1
    assert candidate([1]) == 1

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"


check(count_nums)