import heapq

def k_smallest_pairs(nums1, nums2, k):
    if not nums1 or not nums2 or k <= 0:
        return []

    res = []
    heap = []
    for i in range(min(k, len(nums1))):
        heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

    while k > 0 and heap:
        val, i, j = heapq.heappop(heap)
        res.append([nums1[i], nums2[j]])
        if j + 1 < len(nums2):
            heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        k -= 1

    return res

# Test cases




def check(candidate):
    assert k_smallest_pairs([1,3,7],[2,4,6],2)==[[1, 2], [1, 4]]
    assert k_smallest_pairs([1,3,7],[2,4,6],1)==[[1, 2]]
    assert k_smallest_pairs([1,3,7],[2,4,6],7)==[[1, 2], [1, 4], [3, 2], [1, 6], [3, 4], [3, 6], [7, 2]]

check(k_smallest_pairs)