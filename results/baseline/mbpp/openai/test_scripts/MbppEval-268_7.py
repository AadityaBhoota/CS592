def find_star_num(n):
    if n <= 0:
        return "Invalid input. Please provide a positive integer."

    star_num = n * n * 6 + 1
    return star_num

# Test cases




def check(candidate):
    assert find_star_num(3) == 37
    assert find_star_num(4) == 73
    assert find_star_num(5) == 121

check(find_star_num)