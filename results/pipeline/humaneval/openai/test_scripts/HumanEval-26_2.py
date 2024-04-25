from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    counts = {}  # Step 0: Create an empty dictionary to store the frequency of each element
    for num in numbers:  # Step 1: Iterate through the input list and update the frequency of each element in the dictionary
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
            
    unique_numbers = []  # Step 2: Create a new list to store the unique elements
    for num in numbers:  # Step 3: Create a list to store elements that occur only once
        if counts[num] == 1:
            unique_numbers.append(num)
            
    return unique_numbers  # Step 4: Return the new list containing only unique elements



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([]) == []
    assert candidate([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert candidate([1, 2, 3, 2, 4, 3, 5]) == [1, 4, 5]

check(remove_duplicates)