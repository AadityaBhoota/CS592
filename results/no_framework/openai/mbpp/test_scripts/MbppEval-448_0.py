def cal_sum(n):
    perrin = [3, 0, 2]
    total_sum = sum(perrin[:min(n, 3)])
    
    for i in range(3, n):
        next_perrin = perrin[i-3] + perrin[i-2]
        perrin.append(next_perrin)
        total_sum += next_perrin
    
    return total_sum

# Test cases




def check(candidate):
    assert cal_sum(9) == 49
    assert cal_sum(10) == 66
    assert cal_sum(11) == 88

check(cal_sum)