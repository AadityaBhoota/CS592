def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_ludic(n):
    ludic_numbers = []
    current_num = 1

    while current_num <= n:
        if is_prime(current_num) or any(current_num % num == 0 for num in ludic_numbers):
            ludic_numbers.append(current_num)
        current_num += 1

    return ludic_numbers

# Test cases




def check(candidate):
    assert get_ludic(10) == [1, 2, 3, 5, 7]
    assert get_ludic(25) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25]
    assert get_ludic(45) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25, 29, 37, 41, 43]

check(get_ludic)