def Extract(lst): 
    first_elements = []  # Step 0: Create an empty list to store the first elements of each sublist.
    
    for sub_list in lst:
        first_element = sub_list[0]  # Step 2: Extract the first element of the sublist.
        first_elements.append(first_element)  # Append the first element to the new list.
    
    return first_elements

def check(candidate):
    assert Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6]
    assert Extract([[1,2,3],[4, 5]]) == [1,4]
    assert Extract([[9,8,1],[1,2]]) == [9,1]

check(Extract)