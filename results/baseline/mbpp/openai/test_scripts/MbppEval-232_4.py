def larg_nnum(list1, n):
    # Use heapq to create a min heap
    min_heap = list1[:]
    heapq.heapify(min_heap)
    
    # Pop n largest items from the min heap
    n_largest = []
    while n > 0:
        n_largest.append(heapq.heappop(min_heap))
        n -= 1
    
    return n_largest[::-1]  # Reverse the list to get largest items first

# Testing the function



def check(candidate):
    assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))==set([100,90])
    assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],5))==set([100,90,80,70,60])
    assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],3))==set([100,90,80])

check(larg_nnum)