import heapq

def k_smallest_pairs(nums1, nums2, k):
    if not nums1 or not nums2:
        return []

    pairs = combine_pairs(nums1, nums2)
    sums = sum_pairs(pairs)
    pairs_with_sums = store_pairs_with_sums(pairs, sums)

    min_heap = []
    for pair, total in pairs_with_sums:
        heapq.heappush(min_heap, (-total, pair))
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    k_smallest = [pair for (_, pair) in min_heap]

    return k_smallest

def combine_pairs(nums1, nums2):
    pairs = []
    for num1 in nums1:
        for num2 in nums2:
            pairs.append([num1, num2])
    return pairs

def sum_pairs(pairs):
    return [sum(pair) for pair in pairs]

def store_pairs_with_sums(pairs, sums):
    return [(pairs[i], sums[i]) for i in range(len(pairs))]

def check(candidate):
    assert k_smallest_pairs([1,3,7],[2,4,6],2)==[[1, 2], [1, 4]]
    assert k_smallest_pairs([1,3,7],[2,4,6],1)==[[1, 2]]
    assert k_smallest_pairs([1,3,7],[2,4,6],7)==[[1, 2], [1, 4], [3, 2], [1, 6], [3, 4], [3, 6], [7, 2]]

check(k_smallest_pairs)