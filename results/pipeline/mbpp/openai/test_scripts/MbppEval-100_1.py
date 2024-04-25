def next_smallest_palindrome(num):
    num_str = str(num)
    num_len = len(num_str)

    while True:
        if num_str == num_str[::-1]:
            return int(num_str)
        num += 1
        num_str = str(num)

def get_middle_index(num_len):
    return num_len // 2

def split_number(num_str, middle):
    if len(num_str) % 2 == 0:  # Handle even length
        return num_str[:middle], num_str[middle:]
    else:  # Handle odd length
        return num_str[:middle], num_str[middle+1:]

def mirror_first_half(first_half_str):
    return first_half_str[::-1]

def construct_palindrome(first_half, second_half):
    return int(first_half + second_half)

def check(candidate):
    assert next_smallest_palindrome(99)==101
    assert next_smallest_palindrome(1221)==1331
    assert next_smallest_palindrome(120)==121

check(next_smallest_palindrome)