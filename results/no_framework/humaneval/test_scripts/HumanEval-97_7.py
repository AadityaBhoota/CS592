def multiply(a, b):
    # Get the unit digits of both numbers
    unit_a = abs(a) % 10
    unit_b = abs(b) % 10
    
    # Return the product of the unit digits
    return unit_a * unit_b

# Test cases
print(multiply(148, 412))  # Should return 16
print(multiply(19, 28))    # Should return 72
print(multiply(2020, 1851))    # Should return 0
print(multiply(14, -15))    # Should return 20

def check(candidate):

    # Check some simple cases
    assert candidate(148, 412) == 16, "First test error: " + str(candidate(148, 412))                    
    assert candidate(19, 28) == 72, "Second test error: " + str(candidate(19, 28))           
    assert candidate(2020, 1851) == 0, "Third test error: " + str(candidate(2020, 1851))
    assert candidate(14,-15) == 20, "Fourth test error: " + str(candidate(14,-15))      
    assert candidate(76, 67) == 42, "Fifth test error: " + str(candidate(76, 67))      
    assert candidate(17, 27) == 49, "Sixth test error: " + str(candidate(17, 27))      


    # Check some edge cases that are easy to work out by hand.
    assert candidate(0, 1) == 0, "1st edge test error: " + str(candidate(0, 1))
    assert candidate(0, 0) == 0, "2nd edge test error: " + str(candidate(0, 0))


check(multiply)