def closest_num(N):
    closest_smaller_num = N - 1
    return closest_smaller_num

def check(candidate):
    assert closest_num(11) == 10
    assert closest_num(7) == 6
    assert closest_num(12) == 11

check(closest_num)