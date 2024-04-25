def bell_Number(n):
    if n == 0:
        return 1
    if n == 1:
        return 1

    bell_numbers = [1, 1]
    for i in range(2, n+1):
        bell_num = sum(bell_numbers[j] * bell_numbers[i-j-1] for j in range(i))
        bell_numbers.append(bell_num)

    return bell_numbers[n]

def check(candidate):
    assert bell_Number(2) == 2
    assert bell_Number(3) == 5
    assert bell_Number(4) == 15

check(bell_Number)