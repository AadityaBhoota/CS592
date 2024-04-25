import heapq as hq

def heap_sort(iterable):
    """
    Sort the given list using heap sort.

    Args:
        iterable (list): The list to be sorted.

    Returns:
        list: The sorted list.
    """
    # Step 1: Create a max-heap from the given list
    heap = [-x for x in iterable]
    hq.heapify(heap)

    # Step 2: Repeatedly extract the maximum element from the heap
    result = []
    while heap:
        result.append(-hq.heappop(heap))

    return result

def check(candidate):
    assert heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert heap_sort([25, 35, 22, 85, 14, 65, 75, 25, 58])==[14, 22, 25, 25, 35, 58, 65, 75, 85]
    assert heap_sort( [7, 1, 9, 5])==[1,5,7,9]

check(heap_sort)