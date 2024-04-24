def diff_even_odd(list1):
    even_number = None
    odd_number = None

    for num in list1:
        if num % 2 == 0 and even_number is None:
            even_number = num
        elif num % 2 != 0 and odd_number is None:
            odd_number = num

        if even_number is not None and odd_number is not None:
            break

    if even_number is None or odd_number is None:
        return None

    return abs(even_number - odd_number)

# Test cases




def check(candidate):
    assert diff_even_odd([1,3,5,7,4,1,6,8])==3
    assert diff_even_odd([1,2,3,4,5,6,7,8,9,10])==1
    assert diff_even_odd([1,5,7,9,10])==9

check(diff_even_odd)