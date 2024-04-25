def diff_even_odd(list1):
    even_found = False
    odd_found = False
    for num in list1:
        if not even_found and num % 2 == 0:
            first_even = num
            even_found = True
        elif not odd_found and num % 2 != 0:
            first_odd = num
            odd_found = True
        if even_found and odd_found:
            break
    return abs(first_even - first_odd)

# Test cases




def check(candidate):
    assert diff_even_odd([1,3,5,7,4,1,6,8])==3
    assert diff_even_odd([1,2,3,4,5,6,7,8,9,10])==1
    assert diff_even_odd([1,5,7,9,10])==9

check(diff_even_odd)