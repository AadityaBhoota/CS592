import heapq as hq

def heap_queue_largest(nums, n):
    heap = []
    for num in nums:
        hq.heappush(heap, num)
        if len(heap) > n:
            hq.heappop(heap)
    return sorted(heap, reverse=True)

def check(candidate):
    assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],3)==[85, 75, 65]
    assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],2)==[85, 75]
    assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],5)==[85, 75, 65, 58, 35]

check(heap_queue_largest)