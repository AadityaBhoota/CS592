def odd_num_sum(n):
    num = 1
    sum = 0
    count = 0
    while count < n:
        if num % 2 != 0:
            sum += num ** 4
            count += 1
        num += 1
    return sum

def check(candidate):
    assert odd_num_sum(2) == 82
    assert odd_num_sum(3) == 707
    assert odd_num_sum(4) == 3108

check(odd_num_sum)