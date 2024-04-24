def odd_Equivalent(s, n):
    # Helper function to check if a character is odd
    def is_odd(char):
        return int(char) % 2 == 1

    count_odd = 0
    for i in range(len(s)):
        # Check if the current character in the binary string is odd
        if is_odd(s[i]):
            count_odd += 1

    # Calculate the number of odd numbers after rotating the binary string n times
    remaining_rotations = n % len(s)
    count_after_rotations = (count_odd * n) // len(s)

    return count_after_rotations

# Test cases




def check(candidate):
    assert odd_Equivalent("011001",6) == 3
    assert odd_Equivalent("11011",5) == 4
    assert odd_Equivalent("1010",4) == 2

check(odd_Equivalent)