import heapq

def merge_sorted_list(num1, num2, num3):
    """
    Merge three sorted lists into a single sorted list.

    Args:
        num1 (list): First sorted list.
        num2 (list): Second sorted list.
        num3 (list): Third sorted list.

    Returns:
        list: A single sorted list containing all elements from the three input lists.
    """
    # Create a list of tuples, where each tuple contains an element from one of the input lists and its corresponding list index
    combined = [(x, 0) for x in num1] + [(x, 1) for x in num2] + [(x, 2) for x in num3]
    
    # Sort the combined list using the heap queue
    heapq.heapify(combined)
    
    # Merge the sorted elements into a single list
    result = []
    while combined:
        value, list_index = heapq.heappop(combined)
        result.append(value)
        
        # If there are more elements in the list corresponding to the current index, add them to the heap
        if list_index == 0 and len(num1) > 1:
            heapq.heappush(combined, (num1[1], 0))
            num1.pop(0)
        elif list_index == 1 and len(num2) > 1:
            heapq.heappush(combined, (num2[1], 1))
            num2.pop(0)
        elif list_index == 2 and len(num3) > 1:
            heapq.heappush(combined, (num3[1], 2))
            num3.pop(0)
    
    return result

def check(candidate):
    assert merge_sorted_list([25, 24, 15, 4, 5, 29, 110],[19, 20, 11, 56, 25, 233, 154],[24, 26, 54, 48])==[4, 5, 11, 15, 19, 20, 24, 24, 25, 25, 26, 29, 48, 54, 56, 110, 154, 233]
    assert merge_sorted_list([1, 3, 5, 6, 8, 9], [2, 5, 7, 11], [1, 4, 7, 8, 12])==[1, 1, 2, 3, 4, 5, 5, 6, 7, 7, 8, 8, 9, 11, 12]
    assert merge_sorted_list([18, 14, 10, 9, 8, 7, 9, 3, 2, 4, 1],[25, 35, 22, 85, 14, 65, 75, 25, 58],[12, 74, 9, 50, 61, 41])==[1, 2, 3, 4, 7, 8, 9, 9, 9, 10, 12, 14, 14, 18, 22, 25, 25, 35, 41, 50, 58, 61, 65, 74, 75, 85]

check(merge_sorted_list)