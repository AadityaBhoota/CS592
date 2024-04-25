def closest_num(N):
    if not isinstance(N, int):
        return 'Invalid input. Please enter an integer.'
    
    return N - 1



def check(candidate):
    assert closest_num(11) == 10
    assert closest_num(7) == 6
    assert closest_num(12) == 11

check(closest_num)