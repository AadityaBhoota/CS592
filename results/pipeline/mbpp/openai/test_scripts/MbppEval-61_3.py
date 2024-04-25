from collections import defaultdict
def count_Substrings(s):
    '''
    Write a python function to count the number of substrings with the sum of digits equal to their length.

    Examples:
    count_Substrings('112112',6) == 6
    count_Substrings('111',3) == 6
    count_Substrings('1101112',7) == 12
    '''
def count_substrings(s):
    def sum_of_digits(num):
        return sum(int(digit) for digit in str(num))
    
    count = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substring = s[i:j]
            if sum_of_digits(int(substring)) == len(substring):
                count += 1
                
    return count

def check(candidate):
    assert count_Substrings('112112') == 6
    assert count_Substrings('111') == 6
    assert count_Substrings('1101112') == 12

check(count_Substrings)