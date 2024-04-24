def unique_sublists(list1):
    # Create an empty dictionary to store the count of each sublist
    sublist_count = {}

    # Iterate through the input list
    for sublist in list1:
        # Convert the sublist to a tuple
        sublist_tuple = tuple(sublist)

        # Check if the tuple is already in the dictionary
        if sublist_tuple in sublist_count:
            # If it is, increment the count
            sublist_count[sublist_tuple] += 1
        else:
            # If it's not, add it to the dictionary with a count of 1
            sublist_count[sublist_tuple] = 1

    return sublist_count

def check(candidate):
    assert unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]] )=={(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
    assert unique_sublists([['green', 'orange'], ['black'], ['green', 'orange'], ['white']])=={('green', 'orange'): 2, ('black',): 1, ('white',): 1}
    assert unique_sublists([[10, 20, 30, 40], [60, 70, 50, 50], [90, 100, 200]])=={(10, 20, 30, 40): 1, (60, 70, 50, 50): 1, (90, 100, 200): 1}
    assert unique_sublists([['john']])=={('john',): 1}

check(unique_sublists)