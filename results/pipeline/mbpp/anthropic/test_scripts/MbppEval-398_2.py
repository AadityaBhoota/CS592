def sum_of_digits(nums):
    total_sum = 0
    for num in nums:
        for char in str(num):
            if char.isdigit():
                total_sum += int(char)
    return total_sum

def check(candidate):
    assert sum_of_digits([10,2,56])==14
    assert sum_of_digits([[10,20,4,5,'b',70,'a']])==19
    assert sum_of_digits([10,20,-4,5,-70])==19

check(sum_of_digits)