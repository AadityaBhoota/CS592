import heapq

def k_smallest_pairs(nums1, nums2, k):
    pairs = []
    
    if not nums1 or not nums2 or k == 0:
        return pairs
    
    min_heap = []
    
    for n1 in nums1:
        for n2 in nums2:
            heapq.heappush(min_heap, (n1 + n2, [n1, n2]))
    
    for _ in range(min(k, len(min_heap))):
        pairs.append(heapq.heappop(min_heap)[1])
        
    return pairs

def check(candidate):
    assert k_smallest_pairs([1,3,7],[2,4,6],2)==[[1, 2], [1, 4]]
    assert k_smallest_pairs([1,3,7],[2,4,6],1)==[[1, 2]]
    assert k_smallest_pairs([1,3,7],[2,4,6],7)==[[1, 2], [1, 4], [3, 2], [1, 6], [3, 4], [3, 6], [7, 2]]

check(k_smallest_pairs)