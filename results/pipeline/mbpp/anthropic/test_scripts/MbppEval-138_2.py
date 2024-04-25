def is_Sum_Of_Powers_Of_Two(n):
    if n == 0 or (n & (n - 1)) == 0:
        return True

    result = True
    binary_str = bin(n)[2:]

    for i, char in enumerate(binary_str):
        if char == '1' and 2 ** i != n:
            result = False
            break

    return result

def check(candidate):
    assert is_Sum_Of_Powers_Of_Two(10) == True
    assert is_Sum_Of_Powers_Of_Two(7) == False
    assert is_Sum_Of_Powers_Of_Two(14) == True

check(is_Sum_Of_Powers_Of_Two)