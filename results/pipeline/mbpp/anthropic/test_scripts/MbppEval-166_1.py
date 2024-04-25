def find_even_pair(A):
    even_xor_dict = {}
    count = 0
    for a in A:
        if (a ^ 2) in even_xor_dict:
            count += even_xor_dict[a ^ 2]
        even_xor_dict[a] = even_xor_dict.get(a, 0) + 1
    return count

def check(candidate):
    assert find_even_pair([5, 4, 7, 2, 1]) == 4
    assert find_even_pair([7, 2, 8, 1, 0, 5, 11]) == 9
    assert find_even_pair([1, 2, 3]) == 1

check(find_even_pair)