def find_star_num(n):
    """
    Write a function to find the n'th star number.

    Examples:
    find_star_num(3) == 37
    find_star_num(4) == 73
    find_star_num(5) == 121
    """
    if n == 1:
        return 1
    
    star_num = 1
    for i in range(2, n+1):
        star_num += i
    
    return star_num

def check(candidate):
    assert find_star_num(3) == 37
    assert find_star_num(4) == 73
    assert find_star_num(5) == 121

check(find_star_num)