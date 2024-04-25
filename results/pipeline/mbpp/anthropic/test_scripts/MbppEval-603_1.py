def get_ludic(n):
    ludic_numbers = []
    for i in range(1, n+1):
        if is_ludic(i):
            ludic_numbers.append(i)
    return ludic_numbers

def is_ludic(num):
    if num == 1:
        return True
    
    curr = 1
    while curr < num:
        curr = 2 * curr + 1
    
    return curr == num

def check(candidate):
    assert get_ludic(10) == [1, 2, 3, 5, 7]
    assert get_ludic(25) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25]
    assert get_ludic(45) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25, 29, 37, 41, 43]

check(get_ludic)