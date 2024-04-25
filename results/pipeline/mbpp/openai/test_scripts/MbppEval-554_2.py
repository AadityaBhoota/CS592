def Split(list): 
    odd_integers = []
    
    for num in list:
        if num % 2 != 0:
            odd_integers.append(num)
    
    return odd_integers

def check(candidate):
    assert Split([1,2,3,4,5,6]) == [1,3,5]
    assert Split([10,11,12,13]) == [11,13]
    assert Split([7,8,9,1]) == [7,9,1]

check(Split)