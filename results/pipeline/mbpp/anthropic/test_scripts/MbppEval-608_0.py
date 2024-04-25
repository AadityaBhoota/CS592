def bell_Number(n):
    # Base cases
    if n == 0:
        return 1
    if n == 1:
        return 1
    
    # Recursive case
    bell_sum = 0
    for k in range(n):
        bell_sum += bell_Number(k) * bell_Number(n-k-1)
    return bell_sum

def check(candidate):
    assert bell_Number(2) == 2
    assert bell_Number(3) == 5
    assert bell_Number(4) == 15

check(bell_Number)