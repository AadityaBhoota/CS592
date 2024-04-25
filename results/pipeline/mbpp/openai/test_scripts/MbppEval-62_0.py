def smallest_num(xs):
    # Step 0: Define the function smallest_num
    smallest = xs[0]  # Step 1: Initialize smallest to the first element of the list
    
    # Step 2: Iterate through the list and update the smallest variable if a smaller number is found
    for num in xs:
        if num < smallest:
            smallest = num  # Update smallest if a smaller number is found
    
    return smallest

def check(candidate):
    assert smallest_num([10, 20, 1, 45, 99]) == 1
    assert smallest_num([1, 2, 3]) == 1
    assert smallest_num([45, 46, 50, 60]) == 45

check(smallest_num)