def find_even_pair(A): 
    '''
    Write a function that counts the number of pairs of integers in a list that xor to an even number.

    Examples:
    find_even_Pair([5,4,7,2,1],5) == 4
    find_even_Pair([7,2,8,1,0,5,11],7) == 9
    find_even_Pair([1,2,3],3) == 1
    '''

def check(candidate):
    assert find_even_pair([5, 4, 7, 2, 1]) == 4
    assert find_even_pair([7, 2, 8, 1, 0, 5, 11]) == 9
    assert find_even_pair([1, 2, 3]) == 1

check(find_even_pair)