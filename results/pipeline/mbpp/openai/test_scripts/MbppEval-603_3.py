def get_ludic(n):
    ludic_numbers = []
    
    for num in range(1, n+1):
        is_lucid = True
        for ludic_num in ludic_numbers:
            if num % ludic_num == 0:
                is_lucid = False
                break
        if is_lucid:
            ludic_numbers.append(num)
    
    return ludic_numbers

def check(candidate):
    assert get_ludic(10) == [1, 2, 3, 5, 7]
    assert get_ludic(25) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25]
    assert get_ludic(45) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25, 29, 37, 41, 43]

check(get_ludic)