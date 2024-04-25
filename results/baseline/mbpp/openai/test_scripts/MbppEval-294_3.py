def max_val(listval):
    # Filter out non-numeric values from the list
    numbers = [x for x in listval if isinstance(x, (int, float))]
    
    # Return the maximum value in the list
    return max(numbers) if numbers else None

# Test cases




def check(candidate):
    assert max_val(['Python', 3, 2, 4, 5, 'version'])==5
    assert max_val(['Python', 15, 20, 25])==25
    assert max_val(['Python', 30, 20, 40, 50, 'version'])==50

check(max_val)