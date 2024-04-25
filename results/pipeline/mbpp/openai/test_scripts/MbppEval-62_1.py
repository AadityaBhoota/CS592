def smallest_num(xs):
    smallest = xs[0]
    for num in xs:
        if num < smallest:
            smallest = num
    return smallest

def check(candidate):
    assert smallest_num([10, 20, 1, 45, 99]) == 1
    assert smallest_num([1, 2, 3]) == 1
    assert smallest_num([45, 46, 50, 60]) == 45

check(smallest_num)