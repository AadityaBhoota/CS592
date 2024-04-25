def sort_even(l: list):
    sorted_even_elements = []  # Step 0: Create a new list to store the sorted even elements
    
    for index, element in enumerate(l):  # Step 1: Iterate over the indices and elements of the original list
        if index % 2 == 0:  # Step 2: If the index is even
            sorted_even_elements.append(element)  # Add the element to the sorted_even_elements list
    
    sorted_even_elements.sort()  # Step 3: Sort the elements in the sorted_even_elements list

    index_sorted = 0
    for index, element in enumerate(l):  # Iterating over the indices and elements of the original list again
        if index % 2 == 0:  # If the index is even
            l[index] = sorted_even_elements[index_sorted]  # Replace the element with the sorted element
            index_sorted += 1

    return l  # Step 5: Return the modified list

# Testing the final implementation





METADATA = {}


def check(candidate):
    assert tuple(candidate([1, 2, 3])) == tuple([1, 2, 3])
    assert tuple(candidate([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) == tuple([-10, 3, -5, 2, -3, 3, 5, 0, 9, 1, 123])
    assert tuple(candidate([5, 8, -12, 4, 23, 2, 3, 11, 12, -10])) == tuple([-12, 8, 3, 4, 5, 2, 12, 11, 23, -10])


check(sort_even)