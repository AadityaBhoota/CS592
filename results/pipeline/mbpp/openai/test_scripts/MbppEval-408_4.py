import heapq

def k_smallest_pairs(nums1, nums2, k):
    result = []
    
    pairs = [[num1, num2] for num1 in nums1 for num2 in nums2]
    
    heap = []
    for pair in pairs:
        heapq.heappush(heap, (pair[0] + pair[1], pair))
        if len(heap) > k:
            heapq.heappop(heap)
    
    result = [pair[1] for pair in heap]
    
    return result

def check(candidate):
    assert k_smallest_pairs([1,3,7],[2,4,6],2)==[[1, 2], [1, 4]]
    assert k_smallest_pairs([1,3,7],[2,4,6],1)==[[1, 2]]
    assert k_smallest_pairs([1,3,7],[2,4,6],7)==[[1, 2], [1, 4], [3, 2], [1, 6], [3, 4], [3, 6], [7, 2]]

check(k_smallest_pairs)