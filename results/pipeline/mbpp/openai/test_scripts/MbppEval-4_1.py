import heapq as hq

def heap_queue_largest(nums, n):
    largest_integers = []
    max_heap = [-num for num in nums]
    hq.heapify(max_heap)
    
    for _ in range(n):
        if max_heap:
            largest_integers.append(-hq.heappop(max_heap))
            
    largest_integers = largest_integers[::-1]
    
    return largest_integers

def check(candidate):
    assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],3)==[85, 75, 65]
    assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],2)==[85, 75]
    assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],5)==[85, 75, 65, 58, 35]

check(heap_queue_largest)