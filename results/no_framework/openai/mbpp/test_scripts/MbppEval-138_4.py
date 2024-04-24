def is_Sum_Of_Powers_Of_Two(n):
    # Initialize a variable to store the current power of 2
    power = 1

    # Check if the given number n can be represented as sum of non-zero powers of 2
    while n > 0:
        if n % 2 != 0 and n != 1:
            return False
        n = n // 2
    return True

# Test the function with the examples provided


 
def check(candidate):
    assert is_Sum_Of_Powers_Of_Two(10) == True
    assert is_Sum_Of_Powers_Of_Two(7) == False
    assert is_Sum_Of_Powers_Of_Two(14) == True

check(is_Sum_Of_Powers_Of_Two)