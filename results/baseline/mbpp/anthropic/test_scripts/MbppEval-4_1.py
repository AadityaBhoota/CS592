import heapq as hq

def heap_queue_largest(nums, n):
    """
    Write a function to find the n largest integers from a given list of numbers, returned in descending order.

    Examples:
    heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 3) == [85, 75, 65]
    heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 2) == [85, 75]
    heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 5) == [85, 75, 65, 58, 35]
    """
    # Create a min-heap of the first n elements
    heap = nums[:n]
    hq.heapify(heap)

    # Iterate through the remaining elements
    for i in range(n, len(nums)):
        # If the current element is larger than the smallest element in the heap,
        # replace the smallest element with the current element
        if nums[i] > heap[0]:
            hq.heappop(heap)
            hq.heappush(heap, nums[i])

    # Return the heap in descending order
    return sorted(heap, reverse=True)

def check(candidate):
    assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],3)==[85, 75, 65]
    assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],2)==[85, 75]
    assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],5)==[85, 75, 65, 58, 35]

check(heap_queue_largest)