def next_smallest_palindrome(num):
    num_str = str(num)
    
    n = len(num_str)
    is_odd = n % 2 != 0
    left_half = num_str[:n//2]
    middle_char = num_str[n//2] if is_odd else ''
    
    new_palindrome = left_half + middle_char + left_half[::-1]
    
    return int(new_palindrome)

# Testing the function with examples




def check(candidate):
    assert next_smallest_palindrome(99)==101
    assert next_smallest_palindrome(1221)==1331
    assert next_smallest_palindrome(120)==121

check(next_smallest_palindrome)