def sum_of_digits(nums):
    total = 0
    for num in nums:
        if isinstance(num, (int, float)):
            for digit in str(abs(num)):
                total += int(digit)
    return total

def check(candidate):
    assert sum_of_digits([10,2,56])==14
    assert sum_of_digits([[10,20,4,5,'b',70,'a']])==19
    assert sum_of_digits([10,20,-4,5,-70])==19

check(sum_of_digits)