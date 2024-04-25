def get_ludic(n):
    ludic = [1]
    current = 2

    while current <= n:
        is_ludic = True
        for num in ludic:
            if (current - num) in ludic:
                is_ludic = False
                break
        if is_ludic:
            ludic.append(current)
        current += 1

    return ludic

def check(candidate):
    assert get_ludic(10) == [1, 2, 3, 5, 7]
    assert get_ludic(25) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25]
    assert get_ludic(45) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25, 29, 37, 41, 43]

check(get_ludic)