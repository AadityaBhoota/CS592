def mul_even_odd(list1):
    """
    Write a function to find the product of first even and odd number of a given list.

    Examples:
    mul_even_odd([1,3,5,7,4,1,6,8]) == 4
    mul_even_odd([1,2,3,4,5,6,7,8,9,10]) == 2
    mul_even_odd([1,5,7,9,10]) == 10
    """
    even_found = False
    odd_found = False
    even_num = 1
    odd_num = 1

    for num in list1:
        if num % 2 == 0 and not even_found:
            even_num = num
            even_found = True
        elif num % 2 != 0 and not odd_found:
            odd_num = num
            odd_found = True

        if even_found and odd_found:
            break

    return even_num * odd_num

def check(candidate):
    assert mul_even_odd([1,3,5,7,4,1,6,8])==4
    assert mul_even_odd([1,2,3,4,5,6,7,8,9,10])==2
    assert mul_even_odd([1,5,7,9,10])==10

check(mul_even_odd)