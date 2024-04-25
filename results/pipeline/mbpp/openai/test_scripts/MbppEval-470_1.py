def add_pairwise(test_tup):
    result = []  
    
    for i in range(1, len(test_tup)):
        result.append(test_tup[i-1] + test_tup[i]) 
        
    return tuple(result)  

def check(candidate):
    assert add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)
    assert add_pairwise((2, 6, 8, 9, 11)) == (8, 14, 17, 20)
    assert add_pairwise((3, 7, 9, 10, 12)) == (10, 16, 19, 22)

check(add_pairwise)