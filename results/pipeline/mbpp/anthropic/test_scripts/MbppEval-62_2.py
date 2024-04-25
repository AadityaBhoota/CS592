def smallest_num(xs):
    smallest = xs[0]
    for x in xs[1:]:
        if x < smallest:
            smallest = x
    return smallest

def check(candidate):
    assert smallest_num([10, 20, 1, 45, 99]) == 1
    assert smallest_num([1, 2, 3]) == 1
    assert smallest_num([45, 46, 50, 60]) == 45

check(smallest_num)