def sum_of_digits(nums):
    total_sum = 0
    for item in nums:
        if isinstance(item, (int, float)):
            item = abs(item)
            for digit in str(item):
                total_sum += int(digit)
        elif isinstance(item, list):
            total_sum += sum_of_digits(item)
    return total_sum

def check(candidate):
    assert sum_of_digits([10,2,56])==14
    assert sum_of_digits([[10,20,4,5,'b',70,'a']])==19
    assert sum_of_digits([10,20,-4,5,-70])==19

check(sum_of_digits)