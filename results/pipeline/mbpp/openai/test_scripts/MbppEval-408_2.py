import heapq

def k_smallest_pairs(nums1, nums2, k):
    result = []
    heap = []
    for i in range(min(k, len(nums1))):
        heapq.heappush(heap, (nums1[i], nums2[0], i, 0))

    while k > 0 and heap:
        pair = heapq.heappop(heap)
        result.append([pair[0], pair[1]])
        k -= 1

        if pair[3] < len(nums2) - 1:
            heapq.heappush(heap, (pair[0], nums2[pair[3]+1], pair[2], pair[3] + 1))

    return result

def check(candidate):
    assert k_smallest_pairs([1,3,7],[2,4,6],2)==[[1, 2], [1, 4]]
    assert k_smallest_pairs([1,3,7],[2,4,6],1)==[[1, 2]]
    assert k_smallest_pairs([1,3,7],[2,4,6],7)==[[1, 2], [1, 4], [3, 2], [1, 6], [3, 4], [3, 6], [7, 2]]

check(k_smallest_pairs)