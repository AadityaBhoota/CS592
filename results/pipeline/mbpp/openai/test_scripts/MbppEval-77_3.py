def is_Diff(n):
    even_sum = 0
    odd_sum = 0
    str_n = str(n)
    
    for i in range(len(str_n)):
        if i % 2 == 0:
            even_sum += int(str_n[i])
        else:
            odd_sum += int(str_n[i])
    
    return abs(even_sum - odd_sum) % 11 == 0

def check(candidate):
    assert is_Diff (12345) == False
    assert is_Diff(1212112) == True
    assert is_Diff(1212) == False

check(is_Diff)