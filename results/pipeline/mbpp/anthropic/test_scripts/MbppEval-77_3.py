def is_Diff(n):
    n_str = str(n)
    even_sum = 0
    odd_sum = 0
    
    for i, digit in enumerate(n_str):
        if i % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    
    diff = abs(even_sum - odd_sum)
    return diff % 11 == 0

def check(candidate):
    assert is_Diff (12345) == False
    assert is_Diff(1212112) == True
    assert is_Diff(1212) == False

check(is_Diff)