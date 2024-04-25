def find_even_pair(A):
    xor_set = set()
    count = 0
    
    for num in A:
        current_xor = num
        if current_xor ^ current_xor in xor_set:
            count += 1
        xor_set.add(current_xor)
    
    return count

def check(candidate):
    assert find_even_pair([5, 4, 7, 2, 1]) == 4
    assert find_even_pair([7, 2, 8, 1, 0, 5, 11]) == 9
    assert find_even_pair([1, 2, 3]) == 1

check(find_even_pair)