def diff_even_odd(list1):
    even_index = None
    odd_index = None
    
    for i in range(len(list1)):
        if list1[i] % 2 == 0 and even_index is None:
            even_index = i
        elif list1[i] % 2 != 0 and odd_index is None:
            odd_index = i
            
        if even_index is not None and odd_index is not None:
            break
    
    if even_index is not None and odd_index is not None:
        return abs(list1[even_index] - list1[odd_index])

def check(candidate):
    assert diff_even_odd([1,3,5,7,4,1,6,8])==3
    assert diff_even_odd([1,2,3,4,5,6,7,8,9,10])==1
    assert diff_even_odd([1,5,7,9,10])==9

check(diff_even_odd)