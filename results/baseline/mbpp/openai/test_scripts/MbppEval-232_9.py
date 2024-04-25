import heapq

def larg_nnum(list1, n):
    # Using heapq to maintain a min-heap of size n
    min_heap = list1[:n]
    heapq.heapify(min_heap)
    
    for num in list1[n:]:
        if num > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, num)
    
    # Return the n largest items in descending order
    return sorted(min_heap, reverse=True)

# Test cases




def check(candidate):
    assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))==set([100,90])
    assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],5))==set([100,90,80,70,60])
    assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],3))==set([100,90,80])

check(larg_nnum)