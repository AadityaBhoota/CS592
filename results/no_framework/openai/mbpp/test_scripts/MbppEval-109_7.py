def odd_Equivalent(s, n):
    count = 0
    s_len = len(s)
    
    # Counting the number of odd values in the initial string 's'
    count += sum([int(char) % 2 for char in s])
    
    # Rotating the string 'n' times
    for i in range(1, n):
        # Rotating the string
        s = s[-1] + s[:-1]
        # Counting the number of odd values in the rotated string
        count += sum([int(char) % 2 for char in s])
    
    return count

# Testing the function with the given examples




def check(candidate):
    assert odd_Equivalent("011001",6) == 3
    assert odd_Equivalent("11011",5) == 4
    assert odd_Equivalent("1010",4) == 2

check(odd_Equivalent)