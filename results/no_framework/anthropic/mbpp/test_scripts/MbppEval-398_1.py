def sum_of_digits(nums):
    total = 0
    for num in nums:
        if isinstance(num, int):
            while num != 0:
                total += abs(num % 10)
                num //= 10
    return total

def check(candidate):
    assert sum_of_digits([10,2,56])==14
    assert sum_of_digits([[10,20,4,5,'b',70,'a']])==19
    assert sum_of_digits([10,20,-4,5,-70])==19

check(sum_of_digits)