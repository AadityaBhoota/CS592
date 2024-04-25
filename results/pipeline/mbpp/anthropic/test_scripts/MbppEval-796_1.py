def return_sum(dict_input):
    total_sum = 0
    for value in dict_input.values():
        total_sum += value
    return total_sum

def check(candidate):
    assert return_sum({'a': 100, 'b':200, 'c':300}) == 600
    assert return_sum({'a': 25, 'b':18, 'c':45}) == 88
    assert return_sum({'a': 36, 'b':39, 'c':49}) == 124

check(return_sum)