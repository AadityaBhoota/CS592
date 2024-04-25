import heapq

def calculate_pair_sum(pair):
    return sum(pair)

def k_smallest_pairs(nums1, nums2, k):
    heap = []
    
    for n1 in nums1:
        for n2 in nums2:
            pair = [n1, n2]
            pair_sum = calculate_pair_sum(pair)
            heapq.heappush(heap, (pair_sum, pair))
            
    k_smallest = []
    for _ in range(k):
        if heap:
            k_smallest.append(heapq.heappop(heap)[1])
    
    return k_smallest

def check(candidate):
    assert k_smallest_pairs([1,3,7],[2,4,6],2)==[[1, 2], [1, 4]]
    assert k_smallest_pairs([1,3,7],[2,4,6],1)==[[1, 2]]
    assert k_smallest_pairs([1,3,7],[2,4,6],7)==[[1, 2], [1, 4], [3, 2], [1, 6], [3, 4], [3, 6], [7, 2]]

check(k_smallest_pairs)