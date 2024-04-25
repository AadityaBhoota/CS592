def catalan_number(num):
    if num == 0:
        return 1
    
    catalan = [0] * (num + 1)
    catalan[0] = 1
    catalan[1] = 1
    
    for i in range(2, num + 1):
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i - j - 1]
    
    return catalan[num]

# Test cases




def check(candidate):
    assert catalan_number(10)==16796
    assert catalan_number(9)==4862
    assert catalan_number(7)==429

check(catalan_number)