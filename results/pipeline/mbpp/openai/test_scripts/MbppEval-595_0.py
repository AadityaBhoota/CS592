def min_Swaps(str1, str2):
    swap_count = 0
    
    for bit1, bit2 in zip(str1, str2):
        if bit1 != bit2:
            swap_count += 1
            
    if str1.count('1') != str2.count('1'):
        return "Not Possible"
    
    return swap_count

def check(candidate):
    assert min_Swaps("1101","1110") == 1
    assert min_Swaps("111","000") == "Not Possible"
    assert min_Swaps("111","110") == "Not Possible"

check(min_Swaps)