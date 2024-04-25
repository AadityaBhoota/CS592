def odd_Equivalent(s, n):
    count = 0
    for i in range(n):
        new_s = s[-1] + s[:-1]  # Rotate the binary string by moving the last character to the front
        s = new_s
        
        # Count the number of odd values in the rotated binary string
        count += sum(int(digit) % 2 != 0 for digit in s)
        
    return count

def check(candidate):
    assert odd_Equivalent("011001",6) == 3
    assert odd_Equivalent("11011",5) == 4
    assert odd_Equivalent("1010",4) == 2

check(odd_Equivalent)