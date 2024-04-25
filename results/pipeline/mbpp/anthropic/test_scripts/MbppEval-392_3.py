def get_max_sum (n):
    '''
    Write a function to find the maximum sum possible by using the given equation f(n) = max( (f(n/2) + f(n/3) + f(n/4) + f(n/5)), n).

    Examples:
    get_max_sum(60) == 106
    get_max_sum(10) == 12
    get_max_sum(2) == 2
    '''
def f(n):
    if n <= 1:
        return n
    
    f_n_2 = f(n // 2)
    f_n_3 = f(n // 3)
    f_n_4 = f(n // 4)
    f_n_5 = f(n // 5)
    
    return max(f_n_2 + f_n_3 + f_n_4 + f_n_5, n)

def get_max_sum(n):
    return f(n)

def check(candidate):
    assert get_max_sum(60) == 106
    assert get_max_sum(10) == 12
    assert get_max_sum(2) == 2

check(get_max_sum )