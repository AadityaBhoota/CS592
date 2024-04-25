def is_Diff(n):
    odd_sum = 0
    even_sum = 0
    n_str = str(n)
    
    for i in range(len(n_str)):
        if i % 2 == 0:
            odd_sum += int(n_str[i])
        else:
            even_sum += int(n_str[i])
    
    diff = abs(odd_sum - even_sum)
    return diff % 11 == 0

# Test cases




def check(candidate):
    assert is_Diff (12345) == False
    assert is_Diff(1212112) == True
    assert is_Diff(1212) == False

check(is_Diff)