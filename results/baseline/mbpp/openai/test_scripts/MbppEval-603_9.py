def get_ludic(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    ludic_numbers = [1]
    current_number = 1
    while current_number < n:
        current_number += 1
        if is_prime(current_number) or any(current_number % num == 0 for num in ludic_numbers):
            ludic_numbers.append(current_number)

    return [num for num in ludic_numbers if num <= n]

# Test cases




def check(candidate):
    assert get_ludic(10) == [1, 2, 3, 5, 7]
    assert get_ludic(25) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25]
    assert get_ludic(45) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25, 29, 37, 41, 43]

check(get_ludic)