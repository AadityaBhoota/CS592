import heapq as hq

def heap_queue_largest(nums, n):
    """
    Write a function to find the n largest integers from a given list of numbers, returned in descending order.

    Examples:
    heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 3) == [85, 75, 65]
    heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 2) == [85, 75]
    heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 5) == [85, 75, 65, 58, 35]
    """
    # Use the heapq module to maintain a min-heap of the n largest elements
    heap = []
    for num in nums:
        if len(heap) < n:
            hq.heappush(heap, num)
        elif num > heap[0]:
            hq.heappop(heap)
            hq.heappush(heap, num)
    
    # Return the heap elements in descending order
    return sorted(heap, reverse=True)

def check(candidate):
    assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],3)==[85, 75, 65]
    assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],2)==[85, 75]
    assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],5)==[85, 75, 65, 58, 35]

check(heap_queue_largest)