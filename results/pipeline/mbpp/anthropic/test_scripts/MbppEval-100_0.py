def next_smallest_palindrome(num):
    num_str = str(num)
    
    # If the number is already a palindrome, return the next odd number
    if num_str == num_str[::-1]:
        return num + 1
    
    # Find the middle index of the string
    middle = len(num_str) // 2
    
    # Create the new palindrome string
    left = num_str[:middle]
    right = num_str[middle:][::-1]
    
    # Combine the left and right halves
    new_num_str = left + right
    
    # Convert the new string back to an integer and return it
    return int(new_num_str)

def check(candidate):
    assert next_smallest_palindrome(99)==101
    assert next_smallest_palindrome(1221)==1331
    assert next_smallest_palindrome(120)==121

check(next_smallest_palindrome)