def group_tuples(Input): 
    result = []
    first_elements = {}  # Dictionary to store first element and associated tuples
    
    for tup in Input:
        first_elem = tup[0]
        if first_elem in first_elements:
            first_elements[first_elem].append(tup)
        else:
            first_elements[first_elem] = [tup]
    
    for key in first_elements:
        # Combine all tuples with the common first element
        combined_tuple = tuple(sum(first_elements[key], ()))
        result.append(combined_tuple)
    
    return result
  
# Test cases




def check(candidate):
    assert group_tuples([('x', 'y'), ('x', 'z'), ('w', 't')]) == [('x', 'y', 'z'), ('w', 't')]
    assert group_tuples([('a', 'b'), ('a', 'c'), ('d', 'e')]) == [('a', 'b', 'c'), ('d', 'e')]
    assert group_tuples([('f', 'g'), ('f', 'g'), ('h', 'i')]) == [('f', 'g', 'g'), ('h', 'i')]

check(group_tuples)