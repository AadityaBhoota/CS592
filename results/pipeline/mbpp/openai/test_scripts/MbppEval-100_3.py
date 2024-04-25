def next_smallest_palindrome(num):
    def is_smallest_palindrome(num):
        return str(num) == str(num)[::-1]

    if is_smallest_palindrome(num):
        return num
    else:
        num_str = str(num)
        n = len(num_str)
        mid = n // 2

        left_half = num_str[:mid]
        right_half = num_str[mid + n % 2:]

        # Include the middle digit if the original number has an odd number of digits
        potential_palindrome = int(left_half + num_str[mid] + left_half[::-1])
        return potential_palindrome

# Testing next_smallest_palindrome function with example cases



def check(candidate):
    assert next_smallest_palindrome(99)==101
    assert next_smallest_palindrome(1221)==1331
    assert next_smallest_palindrome(120)==121

check(next_smallest_palindrome)