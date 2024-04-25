def get_ludic(n):
    ludic_numbers = [1]
    current_ludic = 1
    
    while current_ludic <= n:
        next_ludic = current_ludic + len(ludic_numbers)
        ludic_numbers.append(next_ludic)
        current_ludic = next_ludic
    
    return ludic_numbers[:-1]

def check(candidate):
    assert get_ludic(10) == [1, 2, 3, 5, 7]
    assert get_ludic(25) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25]
    assert get_ludic(45) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25, 29, 37, 41, 43]

check(get_ludic)