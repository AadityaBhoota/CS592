def is_palindrome(num):
    return str(num) == str(num)[::-1]

def next_smallest_palindrome(num):
    num += 1
    while not is_palindrome(num):
        num += 1
    return num

# Examples




def check(candidate):
    assert next_smallest_palindrome(99)==101
    assert next_smallest_palindrome(1221)==1331
    assert next_smallest_palindrome(120)==121

check(next_smallest_palindrome)