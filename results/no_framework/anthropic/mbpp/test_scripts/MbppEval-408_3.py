import heapq

def k_smallest_pairs(nums1, nums2, k):
    if not nums1 or not nums2:
        return []

    # Create a min-heap to store the pairs
    heap = [(nums1[0] + nums2[0], 0, 0)]
    result = []

    while k and heap:
        _, i, j = heapq.heappop(heap)
        result.append([nums1[i], nums2[j]])
        k -= 1

        # Add the next pair from the same row or column
        if i + 1 < len(nums1):
            heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
        if j + 1 < len(nums2) and (i == 0 or nums1[i] + nums2[j + 1] < nums1[i - 1] + nums2[j]):
            heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

    return result

def check(candidate):
    assert k_smallest_pairs([1,3,7],[2,4,6],2)==[[1, 2], [1, 4]]
    assert k_smallest_pairs([1,3,7],[2,4,6],1)==[[1, 2]]
    assert k_smallest_pairs([1,3,7],[2,4,6],7)==[[1, 2], [1, 4], [3, 2], [1, 6], [3, 4], [3, 6], [7, 2]]

check(k_smallest_pairs)