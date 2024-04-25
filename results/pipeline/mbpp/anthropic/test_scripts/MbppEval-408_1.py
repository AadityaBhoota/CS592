import heapq

def k_smallest_pairs(nums1, nums2, k):
    result = []
    heap = []

    # Add the first pair to the min-heap
    heapq.heappush(heap, (nums1[0] + nums2[0], 0, 0))

    # Populate the result list
    while len(result) < k and heap:
        _, i, j = heapq.heappop(heap)
        result.append([nums1[i], nums2[j]])

        if j < len(nums2) - 1:
            heapq.heappush(heap, (nums1[i] + nums2[j+1], i, j+1))

    return result

def check(candidate):
    assert k_smallest_pairs([1,3,7],[2,4,6],2)==[[1, 2], [1, 4]]
    assert k_smallest_pairs([1,3,7],[2,4,6],1)==[[1, 2]]
    assert k_smallest_pairs([1,3,7],[2,4,6],7)==[[1, 2], [1, 4], [3, 2], [1, 6], [3, 4], [3, 6], [7, 2]]

check(k_smallest_pairs)