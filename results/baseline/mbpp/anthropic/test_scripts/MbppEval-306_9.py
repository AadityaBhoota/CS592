def max_sum_increasing_subseq(a, n, index, k):
    """
    Find the maximum sum of increasing subsequence from prefix until ith index and also including a given kth element which is after i, i.e., k > i.
    
    Args:
        a (list): List of integers representing the input array.
        n (int): Length of the input array.
        index (int): Index of the element before the kth element.
        k (int): Index of the element to be included in the increasing subsequence.
    
    Returns:
        int: Maximum sum of the increasing subsequence.
    """
    # Base case: If the index is out of range or the kth element is before the index, return 0
    if index >= n or k <= index:
        return 0
    
    # Initialize the maximum sum
    max_sum = 0
    
    # Iterate through the elements from the index to the kth element
    for i in range(index, k):
        # If the current element is less than the kth element, update the maximum sum
        if a[i] < a[k]:
            max_sum = max(max_sum, a[k] + max_sum_increasing_subseq(a, n, i, k))
    
    # Return the maximum sum
    return max_sum

def check(candidate):
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 2, 5) == 7
    assert max_sum_increasing_subseq([11, 15, 19, 21, 26, 28, 31], 7, 2, 4) == 71

check(max_sum_increasing_subseq)