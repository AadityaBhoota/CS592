def get_max_sum (n):
    '''
    Write a function to find the maximum sum possible by using the given equation f(n) = max( (f(n/2) + f(n/3) + f(n/4) + f(n/5)), n).

    Examples:
    get_max_sum(60) == 106
    get_max_sum(10) == 12
    get_max_sum(2) == 2
    '''
def get_max_sum(n):
    # Base case
    if n <= 1:
        return n
    
    # Calculate the maximum possible sum by recursively calling the function for n/2, n/3, n/4, and n/5
    max_sum = max(get_max_sum(n//2), n//2) + \
              max(get_max_sum(n//3), n//3) + \
              max(get_max_sum(n//4), n//4) + \
              max(get_max_sum(n//5), n//5)

    # Calculate the maximum of the sum obtained in step 2 and n
    return max(max_sum, n)

def check(candidate):
    assert get_max_sum(60) == 106
    assert get_max_sum(10) == 12
    assert get_max_sum(2) == 2

check(get_max_sum )