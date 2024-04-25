def cal_sum(n):
    if n == 0:
        return 0
    elif n == 1:
        return 3
    elif n == 2:
        return 3
    else:
        perrin = [3, 0, 2]
        total_sum = sum(perrin)
        for i in range(3, n+1):
            perrin.append(perrin[i-2] + perrin[i-3])
            total_sum += perrin[i]
        return total_sum

# Test the function with the given examples




def check(candidate):
    assert cal_sum(9) == 49
    assert cal_sum(10) == 66
    assert cal_sum(11) == 88

check(cal_sum)