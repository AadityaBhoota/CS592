def find_star_num(n): 
    if n == 1:
        return 3
    
    # Find the n'th star number
    star_num = 3
    for i in range(2, n+1):
        star_num = str(star_num) + str(star_num)
        star_num = int(star_num)
        if i % 2 == 0:
            star_num += 3
        else:
            star_num += 4
    
    return star_num

# Test cases




def check(candidate):
    assert find_star_num(3) == 37
    assert find_star_num(4) == 73
    assert find_star_num(5) == 121

check(find_star_num)