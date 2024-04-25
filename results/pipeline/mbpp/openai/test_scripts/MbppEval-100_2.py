def next_smallest_palindrome(num):
    def is_palindrome(num_str):
        return num_str == num_str[::-1]

    if is_palindrome(str(num)):
        num += 1
        return num
    else:
        num_str = str(num)
        mid = len(num_str) // 2
        left_half = num_str[:mid]
        right_half = num_str[mid + len(num_str) % 2:]
        if int(right_half) < int(left_half[::-1]):
            new_num = int(left_half + left_half[-1] + left_half[::-1])
        else:
            new_num = int(left_half + left_half[-1::-1])

        return new_num

def check(candidate):
    assert next_smallest_palindrome(99)==101
    assert next_smallest_palindrome(1221)==1331
    assert next_smallest_palindrome(120)==121

check(next_smallest_palindrome)