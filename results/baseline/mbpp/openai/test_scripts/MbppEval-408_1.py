def k_smallest_pairs(nums1, nums2, k):
    if not nums1 or not nums2 or k <= 0:
        return []

    heap = []
    
    def push(i, j):
        if i < len(nums1) and j < len(nums2):
            heapq.heappush(heap, (nums1[i] + nums2[j], i, j))
    
    push(0, 0)
    pairs = []
    
    while heap and len(pairs) < k:
        _, i, j = heapq.heappop(heap)
        pairs.append([nums1[i], nums2[j]])
        push(i, j + 1)
        if j == 0:
            push(i + 1, 0)
    
    return pairs

# Test cases




def check(candidate):
    assert k_smallest_pairs([1,3,7],[2,4,6],2)==[[1, 2], [1, 4]]
    assert k_smallest_pairs([1,3,7],[2,4,6],1)==[[1, 2]]
    assert k_smallest_pairs([1,3,7],[2,4,6],7)==[[1, 2], [1, 4], [3, 2], [1, 6], [3, 4], [3, 6], [7, 2]]

check(k_smallest_pairs)