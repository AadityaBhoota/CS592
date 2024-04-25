from collections import defaultdict

def max_occurrences(nums):
    """
    Write a function to find the item with maximum frequency in a given list.

    Examples:
    max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]) == (2, 5)
    max_occurrences([2,3,8,4,7,9,8,7,9,15,14,10,12,13,16,16,18]) == (8, 2)
    max_occurrences([10,20,20,30,40,90,80,50,30,20,50,10]) == (20, 3)
    """
    # Create a dictionary to store the count of each element
    count = defaultdict(int)

    # Iterate through the list and count the occurrences
    for num in nums:
        count[num] += 1

    # Find the element with the maximum count
    max_count = max(count.values())
    max_element = next(key for key, value in count.items() if value == max_count)

    return (max_element, max_count)

def check(candidate):
    assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])==2
    assert max_occurrences([2,3,8,4,7,9,8,7,9,15,14,10,12,13,16,18])==8
    assert max_occurrences([10,20,20,30,40,90,80,50,30,20,50,10])==20

check(max_occurrences)