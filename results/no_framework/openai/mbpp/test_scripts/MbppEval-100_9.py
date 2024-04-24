def next_smallest_palindrome(num):
    def is_palindrome(n):
        return str(n) == str(n)[::-1]
    
    while True:
        num += 1
        if is_palindrome(num):
            return num

# Test cases




def check(candidate):
    assert next_smallest_palindrome(99)==101
    assert next_smallest_palindrome(1221)==1331
    assert next_smallest_palindrome(120)==121

check(next_smallest_palindrome)