def generate_odd_numbers(n):
    odd_numbers = []
    num = 1
    count = 0
    while count < n:
        odd_numbers.append(num)
        num += 2
        count += 1
    return odd_numbers

def calculate_fourth_power(odd_numbers):
    fourth_powers = [num**4 for num in odd_numbers]
    return fourth_powers

def find_sum(fourth_powers):
    return sum(fourth_powers)

def odd_num_sum(n):
    odd_numbers = generate_odd_numbers(n)
    fourth_powers = calculate_fourth_power(odd_numbers)
    result = find_sum(fourth_powers)
    return result

def check(candidate):
    assert odd_num_sum(2) == 82
    assert odd_num_sum(3) == 707
    assert odd_num_sum(4) == 3108

check(odd_num_sum)