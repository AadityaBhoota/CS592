def count_bidirectional(test_list):
    # Create a dictionary to store the count of each tuple pair
    pair_count = {}

    # Iterate through the list of tuples
    for pair in test_list:
        # Check if the pair is bidirectional
        reversed_pair = (pair[1], pair[0])
        if pair in pair_count or reversed_pair in pair_count:
            # If the pair is bidirectional, increment its count
            pair_count[pair] = pair_count.get(pair, 0) + 1
            pair_count[reversed_pair] = pair_count.get(reversed_pair, 0) + 1
        else:
            # Otherwise, add the pair to the dictionary with a count of 1
            pair_count[pair] = 1

    # Count the number of bidirectional pairs
    bidirectional_count = sum(count // 2 for count in pair_count.values())

    return str(bidirectional_count)

def check(candidate):
    assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)] ) == 3
    assert count_bidirectional([(5, 6), (1, 3), (6, 5), (9, 1), (6, 5), (2, 1)] ) == 2
    assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 2), (6, 5), (2, 1)] ) == 4

check(count_bidirectional)