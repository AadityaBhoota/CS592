import heapq

def larg_nnum(list1, n):
    if n <= 0 or n > len(list1):
        return []

    heap = []
    for num in list1:
        heapq.heappush(heap, num)
        if len(heap) > n:
            heapq.heappop(heap)

    return sorted(heap, reverse=True)

# Test cases




def check(candidate):
    assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))==set([100,90])
    assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],5))==set([100,90,80,70,60])
    assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],3))==set([100,90,80])

check(larg_nnum)