def odd_Equivalent(s, n): 
    count = 0
    for i in range(len(s)):
        if s[i] == '1' and n % 2 == 1:
            count += 1
        elif s[i] == '0' and n % 2 == 0:
            count += 1
    return count

# Test cases




def check(candidate):
    assert odd_Equivalent("011001",6) == 3
    assert odd_Equivalent("11011",5) == 4
    assert odd_Equivalent("1010",4) == 2

check(odd_Equivalent)