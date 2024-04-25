def diff_even_odd(list1):
    even_index = None
    odd_index = None

    for i, num in enumerate(list1):
        if num % 2 == 0:
            even_index = i
            break

    for i, num in enumerate(list1):
        if num % 2 != 0:
            odd_index = i
            break

    if even_index is not None and odd_index is not None:
        diff = abs(list1[even_index] - list1[odd_index])
        return diff
    else:
        return None

def check(candidate):
    assert diff_even_odd([1,3,5,7,4,1,6,8])==3
    assert diff_even_odd([1,2,3,4,5,6,7,8,9,10])==1
    assert diff_even_odd([1,5,7,9,10])==9

check(diff_even_odd)