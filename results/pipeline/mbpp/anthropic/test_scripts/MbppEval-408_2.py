import heapq

def k_smallest_pairs(nums1, nums2, k):
    if not nums1 or not nums2:
        return []

    minheap = []
    for num1 in nums1:
        heapq.heappush(minheap, (num1 + nums2[0], num1, nums2[0]))

    result = []
    while k > 0 and minheap:
        _, num1, num2 = heapq.heappop(minheap)
        result.append([num1, num2])
        k -= 1

        if len(nums2) > 1:
            heapq.heappush(minheap, (num1 + nums2[1], num1, nums2[1]))

    return result

def check(candidate):
    assert k_smallest_pairs([1,3,7],[2,4,6],2)==[[1, 2], [1, 4]]
    assert k_smallest_pairs([1,3,7],[2,4,6],1)==[[1, 2]]
    assert k_smallest_pairs([1,3,7],[2,4,6],7)==[[1, 2], [1, 4], [3, 2], [1, 6], [3, 4], [3, 6], [7, 2]]

check(k_smallest_pairs)