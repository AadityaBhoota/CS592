def iscube(a):
    # Taking the absolute value of a to handle negative numbers
    a = abs(a)
    
    # Finding the cube root of a and rounding it to the nearest integer
    root = round(a**(1/3))
    
    # Check if the cube of the rounded root is equal to the original number
    return root**3 == a

# Test cases
print(iscube(1))    # True
print(iscube(2))    # False
print(iscube(-1))   # True
print(iscube(64))   # True
print(iscube(0))    # True
print(iscube(180))  # False

def check(candidate):

    # Check some simple cases
    assert candidate(1) == True, "First test error: " + str(candidate(1))
    assert candidate(2) == False, "Second test error: " + str(candidate(2))
    assert candidate(-1) == True, "Third test error: " + str(candidate(-1))
    assert candidate(64) == True, "Fourth test error: " + str(candidate(64))
    assert candidate(180) == False, "Fifth test error: " + str(candidate(180))
    assert candidate(1000) == True, "Sixth test error: " + str(candidate(1000))


    # Check some edge cases that are easy to work out by hand.
    assert candidate(0) == True, "1st edge test error: " + str(candidate(0))
    assert candidate(1729) == False, "2nd edge test error: " + str(candidate(1728))


check(iscube)