import heapq as hq

def heap_queue_largest(nums, n):
    """
    Write a function to find the n largest integers from a given list of numbers, returned in descending order.

    Examples:
    heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 3) == [85, 75, 65]
    heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 2) == [85, 75]
    heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 5) == [85, 75, 65, 58, 35]
    """
    # Convert the list to a max-heap
    nums = [-x for x in nums]
    hq.heapify(nums)

    # Extract the n largest elements from the heap
    result = [-hq.heappop(nums) for _ in range(n)]
    return result

def check(candidate):
    assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],3)==[85, 75, 65]
    assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],2)==[85, 75]
    assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],5)==[85, 75, 65, 58, 35]

check(heap_queue_largest)