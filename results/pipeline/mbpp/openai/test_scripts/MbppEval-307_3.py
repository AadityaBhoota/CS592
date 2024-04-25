from copy import deepcopy
def colon_tuplex(tuplex, m, n):
    if m < 0 or m >= len(tuplex):
        return "Index out of range"
    
    tup_copy = deepcopy(tuplex)  # Step 1: Create a deep copy of the input tuple
    
    tup_copy = list(tup_copy)  # Step 2: Convert the copied tuple to a list for modification
    
    tup_copy[m] = [n]  # Step 3: Modify the m-th element of the copied tuple to include the value n in a list
    
    return tuple(tup_copy)  # Convert the list back to a tuple for the final result

def check(candidate):
    assert colon_tuplex(("HELLO", 5, [], True) ,2,50)==("HELLO", 5, [50], True)
    assert colon_tuplex(("HELLO", 5, [], True) ,2,100)==(("HELLO", 5, [100],True))
    assert colon_tuplex(("HELLO", 5, [], True) ,2,500)==("HELLO", 5, [500], True)

check(colon_tuplex)