def newman_prime(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def generate_newman_shanks_williams_numbers(length):
        nsw_numbers = [1, 2, 3]
        for i in range(3, length):
            new_num = 2 * nsw_numbers[i-1] + nsw_numbers[i-2] - 2 * nsw_numbers[i-3]
            nsw_numbers.append(new_num)
        return nsw_numbers

    index = 0
    count = 0
    while count < n:
        index += 1
        if is_prime(generate_newman_shanks_williams_numbers(index)[-1]):
            count += 1

    return generate_newman_shanks_williams_numbers(index)[-1]


def check(candidate):
    assert newman_prime(3) == 7
    assert newman_prime(4) == 17
    assert newman_prime(5) == 41

check(newman_prime)