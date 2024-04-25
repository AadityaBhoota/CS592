def count_reverse_pairs(test_list):
    count = 0  # Initialize the count variable

    for i in range(len(test_list)):  # Iterate through the list of strings
        for j in range(i+1, len(test_list)):  # Check if one string is the reverse of the other
            if test_list[i][::-1] == test_list[j]:
                count += 1  # Increment the count by 1

    return str(count)  # Return the count as a string

def check(candidate):
    assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])== 2
    assert count_reverse_pairs(["geeks", "best", "for", "skeeg"]) == 1
    assert count_reverse_pairs(["makes", "best", "sekam", "for", "rof"]) == 2

check(count_reverse_pairs)