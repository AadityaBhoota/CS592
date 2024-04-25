def extract_singly(test_list):
    result = []  # Initialize an empty list to store the final output
    
    for tpl in test_list:  # Iterate over each tuple in the input list
        for num in tpl:  # Iterate over each element in the tuple
            result.append(num)  # Append each element to the result list
    
    return result  # Return the result list with all the elements flattened

def check(candidate):
    assert set(extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)])) == set([3, 4, 5, 7, 1])
    assert set(extract_singly([(1, 2, 3), (4, 2, 3), (7, 8)])) == set([1, 2, 3, 4, 7, 8])
    assert set(extract_singly([(7, 8, 9), (10, 11, 12), (10, 11)])) == set([7, 8, 9, 10, 11, 12])

check(extract_singly)