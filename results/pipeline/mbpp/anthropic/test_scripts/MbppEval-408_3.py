def k_smallest_pairs(nums1, nums2, k):
    pairs = []
    for num1 in nums1:
        for num2 in nums2:
            pairs.append([num1, num2])
    pairs.sort(key=lambda x: x[0] + x[1])
    return pairs[:min(k, len(pairs))]

def check(candidate):
    assert k_smallest_pairs([1,3,7],[2,4,6],2)==[[1, 2], [1, 4]]
    assert k_smallest_pairs([1,3,7],[2,4,6],1)==[[1, 2]]
    assert k_smallest_pairs([1,3,7],[2,4,6],7)==[[1, 2], [1, 4], [3, 2], [1, 6], [3, 4], [3, 6], [7, 2]]

check(k_smallest_pairs)