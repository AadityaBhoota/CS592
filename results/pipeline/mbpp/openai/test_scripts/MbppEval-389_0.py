def find_lucas(n):
    lucas_numbers = [2, 1]  # Lucas(0) and Lucas(1)

    if n <= 1:
        return lucas_numbers[n]
    
    for i in range(2, n+1):
        lucas_numbers.append(lucas_numbers[i-1] + lucas_numbers[i-2])
    
    return lucas_numbers[n]

def check(candidate):
    assert find_lucas(9) == 76
    assert find_lucas(4) == 7
    assert find_lucas(3) == 4

check(find_lucas)