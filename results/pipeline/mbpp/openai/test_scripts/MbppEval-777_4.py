def find_sum(arr):
    unique_elements = set()

    # Step 1: Add unique elements to the set
    for num in arr:
        unique_elements.add(num)

    # Step 2: Calculate the sum of unique elements
    sum_unique = sum(unique_elements)

    return sum_unique

def check(candidate):
    assert find_sum([1,2,3,1,1,4,5,6]) == 21
    assert find_sum([1,10,9,4,2,10,10,45,4]) == 71
    assert find_sum([12,10,9,45,2,10,10,45,10]) == 78

check(find_sum)