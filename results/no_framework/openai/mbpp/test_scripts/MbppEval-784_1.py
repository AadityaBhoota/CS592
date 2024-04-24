def mul_even_odd(list1):
    # Initialize variables to store the first even and odd numbers found
    first_even = None
    first_odd = None

    # Iterate through the list to find the first even and odd numbers
    for num in list1:
        if num % 2 == 0 and first_even is None:  # Check if num is even and first_even is not set
            first_even = num
        elif num % 2 != 0 and first_odd is None:  # Check if num is odd and first_odd is not set
            first_odd = num

        # Break the loop once both the even and odd numbers are found
        if first_even is not None and first_odd is not None:
            break

    # Return the product of the first even and odd numbers if they are found; otherwise return None
    if first_even is not None and first_odd is not None:
        return first_even * first_odd
    else:
        return None

# Test cases




def check(candidate):
    assert mul_even_odd([1,3,5,7,4,1,6,8])==4
    assert mul_even_odd([1,2,3,4,5,6,7,8,9,10])==2
    assert mul_even_odd([1,5,7,9,10])==10

check(mul_even_odd)