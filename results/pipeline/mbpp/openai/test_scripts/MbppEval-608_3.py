from math import comb

def stirling_second(n, k):
    if n == 0 and k == 0:
        return 1
    if n == 0 or k == 0:
        return 0
    return k*stirling_second(n-1, k) + stirling_second(n-1, k-1)

def bell_Number(n):
    bell_numbers = [1, 1]  # Initializing Bell numbers for n = 0, 1
    if n <= 1:
        return bell_numbers[n]
    
    for i in range(2, n+1):
        bell_numbers.append(sum(stirling_second(i-1, j)*bell_numbers[j] for j in range(i)))
    
    return bell_numbers[n]

def check(candidate):
    assert bell_Number(2) == 2
    assert bell_Number(3) == 5
    assert bell_Number(4) == 15

check(bell_Number)