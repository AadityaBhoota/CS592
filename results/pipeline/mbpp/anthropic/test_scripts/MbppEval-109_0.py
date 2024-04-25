def odd_Equivalent(s, n):
    count = 0
    for _ in range(n):
        if int(s, 2) % 2 == 1:
            count += 1
        s = s[-1] + s[:-1]
    return count

def check(candidate):
    assert odd_Equivalent("011001",6) == 3
    assert odd_Equivalent("11011",5) == 4
    assert odd_Equivalent("1010",4) == 2

check(odd_Equivalent)