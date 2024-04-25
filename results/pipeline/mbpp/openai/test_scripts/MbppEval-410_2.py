def min_val(listval):
    min_value = float('inf')
    
    for item in listval:
        if isinstance(item, (int, float)) and item < min_value:  # Step 3
            min_value = item
    
    return min_value  # Step 4

def check(candidate):
    assert min_val(['Python', 3, 2, 4, 5, 'version'])==2
    assert min_val(['Python', 15, 20, 25])==15
    assert min_val(['Python', 30, 20, 40, 50, 'version'])==20

check(min_val)