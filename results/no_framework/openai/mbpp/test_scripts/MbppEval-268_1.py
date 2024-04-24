def find_star_num(n):
    if n <= 0:
        return "Input must be a positive integer."
    
    # Generate a list of star numbers
    star_numbers = []
    i = 1
    while len(star_numbers) < n:
        num = 6*i + 1
        if str(num) == str(num)[::-1]:  # Check if the number is a palindrome
            star_numbers.append(num)
        i += 1
    
    return star_numbers[-1]

# Test cases




def check(candidate):
    assert find_star_num(3) == 37
    assert find_star_num(4) == 73
    assert find_star_num(5) == 121

check(find_star_num)