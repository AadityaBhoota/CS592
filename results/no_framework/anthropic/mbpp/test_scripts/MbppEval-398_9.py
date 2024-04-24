def sum_of_digits(nums):
    """
    Write a function to compute the sum of digits of each number of a given list.

    Examples:
    sum_of_digits([10,2,56]) == 14
    sum_of_digits([[10,20,4,5,'b',70,'a']]) == 19
    sum_of_digits([10,20,-4,5,-70]) == 19
    """
    total_sum = 0

    for num in nums:
        if isinstance(num, (int, float)):
            # Convert the number to a string and sum the digits
            total_sum += sum(int(digit) for digit in str(abs(num)))

    return total_sum

def check(candidate):
    assert sum_of_digits([10,2,56])==14
    assert sum_of_digits([[10,20,4,5,'b',70,'a']])==19
    assert sum_of_digits([10,20,-4,5,-70])==19

check(sum_of_digits)