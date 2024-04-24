def odd_Equivalent(s, n): 
    # Count the number of ones in the original string
    ones_count = s.count('1')
    
    # Check if the count is even
    if ones_count % 2 == 0:
        return len(s)
    
    # Since the count is odd, the number of odd values will be the minimum
    # of ones_count and the length of the string
    return min(ones_count, len(s))

# Test cases




def check(candidate):
    assert odd_Equivalent("011001",6) == 3
    assert odd_Equivalent("11011",5) == 4
    assert odd_Equivalent("1010",4) == 2

check(odd_Equivalent)