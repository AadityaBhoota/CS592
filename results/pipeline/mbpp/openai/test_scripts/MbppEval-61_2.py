from collections import defaultdict

def count_Substrings(s):
    count = 0
    prefix_sums = defaultdict(int)
    prefix_sum = 0
    
    for c in s:
        num = int(c)
        prefix_sum += num
        
        for i in range(1, prefix_sum + 1):
            if prefix_sum - i in prefix_sums:
                count += prefix_sums[prefix_sum - i]
        
        prefix_sums[prefix_sum] += 1
    
    return count

def check(candidate):
    assert count_Substrings('112112') == 6
    assert count_Substrings('111') == 6
    assert count_Substrings('1101112') == 12

check(count_Substrings)