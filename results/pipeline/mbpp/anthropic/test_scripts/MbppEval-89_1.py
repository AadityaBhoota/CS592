def closest_num(N):
    if N < 0:
        return N - 1
    
    N_str = str(N)
    last_digit = int(N_str[-1])
    
    if last_digit == 0:
        return N - 1
    else:
        new_last_digit = last_digit - 1
        new_N_str = N_str[:-1] + str(new_last_digit)
        return int(new_N_str)

def check(candidate):
    assert closest_num(11) == 10
    assert closest_num(7) == 6
    assert closest_num(12) == 11

check(closest_num)