def cal_sum(n): 
    if n <= 0:
        return 0
    elif n <= 2:
        return n
    else:
        a, b, c = 3, 0, 2
        total_sum = 5
        
        for i in range(3, n+1):
            val = a + b
            a, b, c = b, c, val
            total_sum += val
        
        return total_sum

# Examples




def check(candidate):
    assert cal_sum(9) == 49
    assert cal_sum(10) == 66
    assert cal_sum(11) == 88

check(cal_sum)