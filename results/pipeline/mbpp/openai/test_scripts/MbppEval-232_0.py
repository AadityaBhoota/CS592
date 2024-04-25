import heapq

def larg_nnum(list1, n):
    max_heap = list1[:]
    heapq.heapify(max_heap)
    
    neg_max_heap = [-x for x in max_heap]
    heapq.heapify(neg_max_heap)
    
    n_largest = []
    for i in range(n):
        n_largest.append(-heapq.heappop(neg_max_heap))
    
    return n_largest

def check(candidate):
    assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))==set([100,90])
    assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],5))==set([100,90,80,70,60])
    assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],3))==set([100,90,80])

check(larg_nnum)