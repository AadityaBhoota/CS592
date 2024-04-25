def find_lucas(n):
    """
    Write a function to find the n'th lucas number.

    Examples:
    find_lucas(9) == 76
    find_lucas(4) == 7
    find_lucas(3) == 4
    """
    lucas_numbers = [2, 1]  # Initialize the list with the first two Lucas numbers

    if n < 2:
        return lucas_numbers[n]

    # Calculate and store the remaining Lucas numbers
    for i in range(2, n + 1):
        next_lucas = lucas_numbers[i - 1] + lucas_numbers[i - 2]
        lucas_numbers.append(next_lucas)

    return lucas_numbers[n]

def check(candidate):
    assert find_lucas(9) == 76
    assert find_lucas(4) == 7
    assert find_lucas(3) == 4

check(find_lucas)