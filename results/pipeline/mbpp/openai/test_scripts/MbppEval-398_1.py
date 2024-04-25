def sum_of_digits(nums):
    total_sum = 0

    if not nums:
        return total_sum

    for num in nums:
        if isinstance(num, (int, str)):
            num_str = str(num)
            num_sum = 0
            for digit in num_str:
                if digit.isdigit():
                    num_sum += int(digit)
            total_sum += num_sum

    return total_sum

def check(candidate):
    assert sum_of_digits([10,2,56])==14
    assert sum_of_digits([[10,20,4,5,'b',70,'a']])==19
    assert sum_of_digits([10,20,-4,5,-70])==19

check(sum_of_digits)