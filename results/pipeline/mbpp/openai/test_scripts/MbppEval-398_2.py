def sum_of_digits(nums):
    total_sum = 0

    for num in nums:
        if isinstance(num, int):
            digit_sum = 0
            for digit in str(num):
                if digit.isdigit():
                    digit_sum += int(digit)
            total_sum += digit_sum
        else:
            print(f"Ignoring non-integer element: {num}")

    return total_sum

def check(candidate):
    assert sum_of_digits([10,2,56])==14
    assert sum_of_digits([[10,20,4,5,'b',70,'a']])==19
    assert sum_of_digits([10,20,-4,5,-70])==19

check(sum_of_digits)