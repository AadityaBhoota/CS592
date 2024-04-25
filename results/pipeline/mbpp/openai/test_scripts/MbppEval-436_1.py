def neg_nos(list1):
    neg_nums = []  # Create an empty list to store negative numbers
    
    for num in list1:
        if num < 0:
            neg_nums.append(num)  # Append negative number to the list
    
    return neg_nums  # Return the list of negative numbers

def check(candidate):
    assert neg_nos([-1,4,5,-6]) == [-1,-6]
    assert neg_nos([-1,-2,3,4]) == [-1,-2]
    assert neg_nos([-7,-6,8,9]) == [-7,-6]

check(neg_nos)