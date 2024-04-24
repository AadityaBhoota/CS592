def odd_Equivalent(s, n):
    s += s  # Concatenate the string with itself to simulate rotation
    count = 0
    for i in range(len(s)):
        if int(s[i], 2) % 2 == 1:  # Checking if the number is odd
            count += 1
    return count

# Test cases




def check(candidate):
    assert odd_Equivalent("011001",6) == 3
    assert odd_Equivalent("11011",5) == 4
    assert odd_Equivalent("1010",4) == 2

check(odd_Equivalent)