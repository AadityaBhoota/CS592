def closest_num(N):
    smaller_num = N - 1
    if smaller_num < N:
        return smaller_num
    else:
        return "No smaller number found"

def check(candidate):
    assert closest_num(11) == 10
    assert closest_num(7) == 6
    assert closest_num(12) == 11

check(closest_num)