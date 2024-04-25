import heapq

def k_smallest_pairs(nums1, nums2, k):
    if not nums1 or not nums2:
        return []

    min_heap = []
    for x in nums1:
        for y in nums2:
            pair_sum = x + y
            heapq.heappush(min_heap, (pair_sum, x, y))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

    return [[x, y] for _, x, y in min_heap]

def check(candidate):
    assert k_smallest_pairs([1,3,7],[2,4,6],2)==[[1, 2], [1, 4]]
    assert k_smallest_pairs([1,3,7],[2,4,6],1)==[[1, 2]]
    assert k_smallest_pairs([1,3,7],[2,4,6],7)==[[1, 2], [1, 4], [3, 2], [1, 6], [3, 4], [3, 6], [7, 2]]

check(k_smallest_pairs)