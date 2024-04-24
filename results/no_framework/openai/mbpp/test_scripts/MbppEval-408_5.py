import heapq

def k_smallest_pairs(nums1, nums2, k):
    if not nums1 or not nums2 or k <= 0:
        return []

    heap = []
    for i in range(min(k, len(nums1))):
        heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

    result = []
    while len(result) < k and heap:
        sum_val, i, j = heapq.heappop(heap)
        result.append([nums1[i], nums2[j]])
        if j + 1 < len(nums2):
            new_sum = nums1[i] + nums2[j + 1]
            heapq.heappush(heap, (new_sum, i, j + 1))

    return result

# Test cases




def check(candidate):
    assert k_smallest_pairs([1,3,7],[2,4,6],2)==[[1, 2], [1, 4]]
    assert k_smallest_pairs([1,3,7],[2,4,6],1)==[[1, 2]]
    assert k_smallest_pairs([1,3,7],[2,4,6],7)==[[1, 2], [1, 4], [3, 2], [1, 6], [3, 4], [3, 6], [7, 2]]

check(k_smallest_pairs)