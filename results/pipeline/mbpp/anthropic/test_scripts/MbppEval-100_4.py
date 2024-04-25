def next_smallest_palindrome(num):
    num_str = str(num)
    
    if num_str == num_str[::-1]:
        return num
    
    if len(num_str) % 2 == 1:
        middle_digit = int(num_str[len(num_str) // 2])
        new_middle_digit = middle_digit + 1
        new_num_str = num_str[:len(num_str) // 2] + str(new_middle_digit) + num_str[len(num_str) // 2 + 1:][::-1]
    else:
        left_half = num_str[:len(num_str) // 2]
        right_half = num_str[len(num_str) // 2:]
        if int(left_half[-1]) < int(right_half[0]):
            new_right_half = str(int(right_half[0]) + 1) + right_half[1:]
        else:
            new_right_half = str(int(right_half[0])) + right_half[1:]
        new_num_str = left_half + new_right_half[::-1]
    
    return int(new_num_str)

def check(candidate):
    assert next_smallest_palindrome(99)==101
    assert next_smallest_palindrome(1221)==1331
    assert next_smallest_palindrome(120)==121

check(next_smallest_palindrome)