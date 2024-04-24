from collections import defaultdict

def max_occurrences(nums):
    """
    Finds the item with maximum frequency in a given list.

    Args:
        nums (list): A list of numbers.

    Returns:
        tuple: A tuple containing the item with maximum frequency and its count.
    """
    # Create a defaultdict to store the count of each item
    count = defaultdict(int)

    # Count the occurrence of each item
    for num in nums:
        count[num] += 1

    # Find the item with maximum frequency
    max_count = max(count.values())
    max_item = next(item for item, c in count.items() if c == max_count)

    return (max_item, max_count)

def check(candidate):
    assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])==2
    assert max_occurrences([2,3,8,4,7,9,8,7,9,15,14,10,12,13,16,18])==8
    assert max_occurrences([10,20,20,30,40,90,80,50,30,20,50,10])==20

check(max_occurrences)