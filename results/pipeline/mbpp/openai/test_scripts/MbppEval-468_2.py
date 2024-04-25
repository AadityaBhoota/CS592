from typing import List

def max_product(arr: List[int]) -> int:
    if not arr:
        return 0
    
    n = len(arr)
    max_product = arr[0]
    
    increasing_subsequences = [[arr[0]]]
    
    for i in range(1, n):
        current = arr[i]
        new_sequences = []
        
        for seq in increasing_subsequences:
            if current > seq[-1]:
                new_sequences.append(seq + [current])
                
        increasing_subsequences.extend(new_sequences)
        increasing_subsequences.append([current])
    
    max_prod = float('-inf')
    for seq in increasing_subsequences:
        product = 1
        for num in seq:
            product *= num
        max_prod = max(max_prod, product)
    
    return max_prod

def check(candidate):
    assert max_product([3, 100, 4, 5, 150, 6]) == 3000
    assert max_product([4, 42, 55, 68, 80]) == 50265600
    assert max_product([10, 22, 9, 33, 21, 50, 41, 60]) == 2460

check(max_product)