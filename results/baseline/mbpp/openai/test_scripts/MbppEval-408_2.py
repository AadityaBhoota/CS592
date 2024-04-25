import heapq

def k_smallest_pairs(nums1, nums2, k):
    if not nums1 or not nums2:
        return []

    # Initialize a priority queue to keep track of the pairs
    pq = []
    
    # Create a helper function to handle insertion into the priority queue
    def push(i, j):
        if i < len(nums1) and j < len(nums2):
            heapq.heappush(pq, (nums1[i] + nums2[j], i, j))

    # Initialize the result list to store the k smallest pairs
    result = []
    
    # Push the first pair (nums1[0], nums2[0]) into the priority queue
    push(0, 0)
    
    # While there are more pairs to consider and we have not yet found k pairs
    while pq and len(result) < k:
        _, i, j = heapq.heappop(pq)
        result.append([nums1[i], nums2[j]])
        
        # Push the next possible pairs (nums1[i], nums2[j+1]) and (nums1[i+1], nums2[j])
        push(i, j + 1)
        if j == 0:
            push(i + 1, j)
    
    return result

# Test the function with example cases




def check(candidate):
    assert k_smallest_pairs([1,3,7],[2,4,6],2)==[[1, 2], [1, 4]]
    assert k_smallest_pairs([1,3,7],[2,4,6],1)==[[1, 2]]
    assert k_smallest_pairs([1,3,7],[2,4,6],7)==[[1, 2], [1, 4], [3, 2], [1, 6], [3, 4], [3, 6], [7, 2]]

check(k_smallest_pairs)