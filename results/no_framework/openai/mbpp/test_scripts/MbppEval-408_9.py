import heapq

def k_smallest_pairs(nums1, nums2, k):
    if not nums1 or not nums2:
        return []

    heap = []
    for n1 in nums1:
        for n2 in nums2:
            heapq.heappush(heap, (n1 + n2, [n1, n2]))  # Push pair sum and pair itself

    ans = []
    while k > 0 and heap:
        ans.append(heapq.heappop(heap)[1])  # Get the pair with the smallest sum
        k -= 1

    return ans

# Test cases




def check(candidate):
    assert k_smallest_pairs([1,3,7],[2,4,6],2)==[[1, 2], [1, 4]]
    assert k_smallest_pairs([1,3,7],[2,4,6],1)==[[1, 2]]
    assert k_smallest_pairs([1,3,7],[2,4,6],7)==[[1, 2], [1, 4], [3, 2], [1, 6], [3, 4], [3, 6], [7, 2]]

check(k_smallest_pairs)