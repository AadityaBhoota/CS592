def diff_even_odd(list1):
    even_found = False
    odd_found = False
    for num in list1:
        if num % 2 == 0 and not even_found:
            even_number = num
            even_found = True
        elif num % 2 != 0 and not odd_found:
            odd_number = num
            odd_found = True
        if even_found and odd_found:
            break
    return abs(even_number - odd_number) if even_found and odd_found else None

# Test cases




def check(candidate):
    assert diff_even_odd([1,3,5,7,4,1,6,8])==3
    assert diff_even_odd([1,2,3,4,5,6,7,8,9,10])==1
    assert diff_even_odd([1,5,7,9,10])==9

check(diff_even_odd)