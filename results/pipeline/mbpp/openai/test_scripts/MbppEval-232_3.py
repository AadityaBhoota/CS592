import heapq

def larg_nnum(list1, n):
    n_largest = []
    heap = []

    for ele in list1:
        heapq.heappush(heap, ele)
        if len(heap) > n:
            heapq.heappop(heap)

    return heap

def check(candidate):
    assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))==set([100,90])
    assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],5))==set([100,90,80,70,60])
    assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],3))==set([100,90,80])

check(larg_nnum)