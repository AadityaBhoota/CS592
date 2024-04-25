def calculate_digit_sum(s):
    return sum(int(d) for d in s)

def is_valid_substring(sub):
    return calculate_digit_sum(sub) == len(sub)

def count_Substrings(s):
    count = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if is_valid_substring(s[i:j]):
                count += 1
                
    return count

def check(candidate):
    assert count_Substrings('112112') == 6
    assert count_Substrings('111') == 6
    assert count_Substrings('1101112') == 12

check(count_Substrings)