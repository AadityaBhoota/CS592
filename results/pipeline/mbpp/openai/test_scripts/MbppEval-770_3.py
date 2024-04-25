def odd_num_sum(n):
    result = 0
    count = 0
    
    for i in range(1, n*2, 2):
        result += i**4
        count += 1
        if count == n:
            break
        
    return result

def check(candidate):
    assert odd_num_sum(2) == 82
    assert odd_num_sum(3) == 707
    assert odd_num_sum(4) == 3108

check(odd_num_sum)