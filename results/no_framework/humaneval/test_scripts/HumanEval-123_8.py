def get_odd_collatz(n):
    # Helper function to generate the collatz sequence for a given number
    def collatz_sequence(num):
        sequence = [num]
        while num != 1:
            if num % 2 == 0:
                num = num // 2
            else:
                num = 3 * num + 1
            sequence.append(num)
        return sequence
    
    # Generating the collatz sequence for the input number and filtering out the odd numbers
    collatz_list = collatz_sequence(n)
    odd_numbers = sorted(set(num for num in collatz_list if num % 2 == 1))
    
    return odd_numbers

# Test the function with an example
print(get_odd_collatz(5))  # Output: [1, 5]

def check(candidate):

    # Check some simple cases
    assert candidate(14) == [1, 5, 7, 11, 13, 17]
    assert candidate(5) == [1, 5]
    assert candidate(12) == [1, 3, 5], "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert candidate(1) == [1], "This prints if this assert fails 2 (also good for debugging!)"


check(get_odd_collatz)