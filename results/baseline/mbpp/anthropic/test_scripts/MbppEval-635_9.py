import heapq as hq

def heap_sort(iterable):
    """
    Write a function to sort the given list.

    Examples:
    heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    heap_sort([25, 35, 22, 85, 14, 65, 75, 25, 58]) == [14, 22, 25, 25, 35, 58, 65, 75, 85]
    heap_sort([7, 1, 9, 5]) == [1, 5, 7, 9]
    """
    # Build a min-heap from the input list
    heap = [-x for x in iterable]
    hq.heapify(heap)

    # Extract elements from the heap one by one and add them to the result list
    result = []
    while heap:
        result.append(-hq.heappop(heap))

    return result

def check(candidate):
    assert heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert heap_sort([25, 35, 22, 85, 14, 65, 75, 25, 58])==[14, 22, 25, 25, 35, 58, 65, 75, 85]
    assert heap_sort( [7, 1, 9, 5])==[1,5,7,9]

check(heap_sort)