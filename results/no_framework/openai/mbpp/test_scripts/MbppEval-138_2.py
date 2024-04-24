def is_Sum_Of_Powers_Of_Two(n):
    # Function to check if a number is a power of 2
    def is_power_of_2(num):
        return num != 0 and (num & (num - 1)) == 0

    # Iterate over powers of 2 and check if their sum equals n
    for i in range(1, n):
        if is_power_of_2(n-i):
            return True
    return False

# Test cases




def check(candidate):
    assert is_Sum_Of_Powers_Of_Two(10) == True
    assert is_Sum_Of_Powers_Of_Two(7) == False
    assert is_Sum_Of_Powers_Of_Two(14) == True

check(is_Sum_Of_Powers_Of_Two)