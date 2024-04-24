def get_ludic(n):
    ludic_numbers = [1]
    potential_ludics = [2]  # We start from 2 as the first ludic number

    while potential_ludics:
        next_ludic = potential_ludics.pop(0)
        if next_ludic <= n:
            ludic_numbers.append(next_ludic)
            potential_ludics.extend([next_ludic + i for i in range(1, n) if (next_ludic + i) not in potential_ludics])

    return ludic_numbers

# Test cases




def check(candidate):
    assert get_ludic(10) == [1, 2, 3, 5, 7]
    assert get_ludic(25) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25]
    assert get_ludic(45) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25, 29, 37, 41, 43]

check(get_ludic)