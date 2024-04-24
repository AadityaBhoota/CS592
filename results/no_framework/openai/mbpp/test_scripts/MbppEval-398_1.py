def sum_of_digits(nums):
    total_sum = 0
    for num in nums:
        try:
            if isinstance(num, int):
                num = abs(num)
                while num > 0:
                    total_sum += num % 10
                    num //= 10
            elif isinstance(num, list):
                total_sum += sum_of_digits(num)
        except (ValueError, TypeError):
            continue
    return total_sum

# Tests




def check(candidate):
    assert sum_of_digits([10,2,56])==14
    assert sum_of_digits([[10,20,4,5,'b',70,'a']])==19
    assert sum_of_digits([10,20,-4,5,-70])==19

check(sum_of_digits)