def count_bidirectional(test_list):
    """
    Write a function to count bidirectional tuple pairs.

    Examples:
    count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)]) == '3'
    count_bidirectional([(5, 6), (1, 3), (6, 5), (9, 1), (6, 5), (2, 1)]) == '2'
    count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 2), (6, 5), (2, 1)]) == '4'
    """
    # Create a dictionary to store the count of each tuple pair
    pair_count = {}

    # Iterate through the list of tuples
    for pair in test_list:
        # Reverse the tuple and check if it exists in the dictionary
        reverse_pair = (pair[1], pair[0])
        if reverse_pair in pair_count:
            # If it exists, increment the count
            pair_count[reverse_pair] += 1
        else:
            # If it doesn't exist, add it to the dictionary with a count of 1
            pair_count[pair] = 1

    # Count the number of bidirectional pairs
    bidirectional_count = 0
    for count in pair_count.values():
        if count > 1:
            bidirectional_count += 1

    return str(bidirectional_count)

def check(candidate):
    assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)] ) == 3
    assert count_bidirectional([(5, 6), (1, 3), (6, 5), (9, 1), (6, 5), (2, 1)] ) == 2
    assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 2), (6, 5), (2, 1)] ) == 4

check(count_bidirectional)