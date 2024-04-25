import sys

def next_smallest_palindrome(num):
    def is_palindrome(num_str):
        return num_str == num_str[::-1]
    
    num_str = str(num)
    if is_palindrome(num_str):
        return num
    else:
        return None

# Implementing step 2 correctly
def next_smallest_palindrome(num):
    def is_palindrome(num_str):
        return num_str == num_str[::-1]
    
    num_str = str(num)
    if is_palindrome(num_str):
        return num
    else:
        return int(num_str)





def check(candidate):
    assert next_smallest_palindrome(99)==101
    assert next_smallest_palindrome(1221)==1331
    assert next_smallest_palindrome(120)==121

check(next_smallest_palindrome)