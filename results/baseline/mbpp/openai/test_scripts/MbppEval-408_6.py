import heapq

def k_smallest_pairs(nums1, nums2, k):
    if not nums1 or not nums2 or k <= 0:
        return []
    
    heap = []
    for num1 in nums1:
        for num2 in nums2:
            heapq.heappush(heap, (num1 + num2, [num1, num2]))
    
    result = []
    for _ in range(min(k, len(heap))):
        result.append(heapq.heappop(heap)[1])
    
    return result

# Test cases




def check(candidate):
    assert k_smallest_pairs([1,3,7],[2,4,6],2)==[[1, 2], [1, 4]]
    assert k_smallest_pairs([1,3,7],[2,4,6],1)==[[1, 2]]
    assert k_smallest_pairs([1,3,7],[2,4,6],7)==[[1, 2], [1, 4], [3, 2], [1, 6], [3, 4], [3, 6], [7, 2]]

check(k_smallest_pairs)