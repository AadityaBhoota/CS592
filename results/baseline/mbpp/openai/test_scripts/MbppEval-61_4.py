def count_Substrings(s):
    count = 0
    n = len(s)
    
    for i in range(n):
        sum_digits = 0
        for j in range(i, n):
            sum_digits += int(s[j])
            if sum_digits == j-i+1:
                count += 1
    
    return count

# Test the function



def check(candidate):
    assert count_Substrings('112112') == 6
    assert count_Substrings('111') == 6
    assert count_Substrings('1101112') == 12

check(count_Substrings)