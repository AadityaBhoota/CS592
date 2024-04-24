def odd_Equivalent(s, n):
    count = 0
    for i in range(n):
        binary = int(s, 2)
        binary = (binary << 1) | (binary >> (len(s) - 1))
        binary = binary % (2 ** len(s))
        s = f"{binary:0{len(s)}b}"
        if int(s, 2) % 2 == 1:
            count += 1
    return count

def check(candidate):
    assert odd_Equivalent("011001",6) == 3
    assert odd_Equivalent("11011",5) == 4
    assert odd_Equivalent("1010",4) == 2

check(odd_Equivalent)