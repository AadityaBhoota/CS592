def calculate_perrin_number(n):
    if n == 0:
        return 3
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    
    perrin = [3, 0, 2]
    
    for i in range(3, n+1):
        next_perrin = perrin[-2] + perrin[-3]
        perrin.append(next_perrin)
    
    return perrin[n]

def cal_sum(n):
    total_sum = sum(calculate_perrin_number(i) for i in range(n))  # Calculate the sum of first n Perrin numbers
    return total_sum

# Test the function




def check(candidate):
    assert cal_sum(9) == 49
    assert cal_sum(10) == 66
    assert cal_sum(11) == 88

check(cal_sum)