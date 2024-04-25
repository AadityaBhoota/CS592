def cal_sum(n):
    if n <= 2:
        return 0

    perrin_numbers = [3, 0, 2]
    total_sum = sum(perrin_numbers)

    for i in range(3, n):
        next_num = perrin_numbers[i-3] + perrin_numbers[i-2]
        perrin_numbers.append(next_num)
        total_sum += next_num

    return total_sum

# Test cases




def check(candidate):
    assert cal_sum(9) == 49
    assert cal_sum(10) == 66
    assert cal_sum(11) == 88

check(cal_sum)