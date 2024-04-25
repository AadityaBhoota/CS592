def next_smallest_palindrome(num):
    num_str = str(num)
    length = len(num_str)
    
    if length == 1:
        return num + 1
    
    middle = length // 2
    left = num_str[:middle]
    right = num_str[middle:] if length % 2 == 0 else num_str[middle  + 1:]
    
    left_mirror = left[::-1]
    if int(left_mirror) > int(right):
        next_palindrome = left + left_mirror
    else:
        left_incremented = str(int(left) + 1)
        if len(left_incremented) > len(left):
            next_palindrome = left_incremented + left_incremented[:-1][::-1]
        else:
            next_palindrome = left_incremented + left_incremented[::-1]
    
    if length % 2 != 0:
        next_palindrome = next_palindrome[:-1]
    
    return int(next_palindrome)

# Test cases




def check(candidate):
    assert next_smallest_palindrome(99)==101
    assert next_smallest_palindrome(1221)==1331
    assert next_smallest_palindrome(120)==121

check(next_smallest_palindrome)