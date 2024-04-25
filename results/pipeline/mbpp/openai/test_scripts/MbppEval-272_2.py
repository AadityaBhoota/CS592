def rear_extract(test_list):
    rear_elements = []  # Step 0: Create an empty list to store the rear elements of the tuples.
    
    for tup in test_list:  # Step 1: Iterate through each tuple in the input list.
        rear_element = tup[-1]  # Step 2: Get the last element (rear element) of the tuple.
        rear_elements.append(rear_element)  # Step 3: Append the rear element to the list.
        
    return rear_elements  # Step 4: Return the list containing the rear elements.

def check(candidate):
    assert rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]) == [21, 20, 19]
    assert rear_extract([(1, 'Sai', 36), (2, 'Ayesha', 25), (3, 'Salman', 45)]) == [36, 25, 45]
    assert rear_extract([(1, 'Sudeep', 14), (2, 'Vandana', 36), (3, 'Dawood', 56)]) == [14, 36, 56]

check(rear_extract)