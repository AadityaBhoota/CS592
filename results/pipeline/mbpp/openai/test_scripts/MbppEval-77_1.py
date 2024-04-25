def is_Diff(n): 
    sum_alt_digits = 0
    for i, digit in enumerate(str(n)):
        if i % 2 == 0:
            sum_alt_digits += int(digit)
        else:
            sum_alt_digits -= int(digit)

    return sum_alt_digits % 11 == 0

def check(candidate):
    assert is_Diff (12345) == False
    assert is_Diff(1212112) == True
    assert is_Diff(1212) == False

check(is_Diff)