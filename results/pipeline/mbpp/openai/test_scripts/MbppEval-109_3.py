def odd_Equivalent(s, n):
    count = 0

    if s.count('1') % 2 != 0:
        count += 1

    for i in range(n):
        ones_count = s.count('1')
        if ones_count % 2 != 0:
            count += 1
        s = s[1:] + s[0]

    return count

def check(candidate):
    assert odd_Equivalent("011001",6) == 3
    assert odd_Equivalent("11011",5) == 4
    assert odd_Equivalent("1010",4) == 2

check(odd_Equivalent)