def kth_element(arr, k, index=1):
    """
    Find the kth element in the given array using 1-based indexing.

    Args:
        arr (list): The input array.
        k (int): The value of k.
        index (int, optional): The 1-based index. Defaults to 1.

    Returns:
        int: The kth element in the array.
    """
    if k < 1 or k > len(arr):
        return "Error: k is not within the valid range of the array length."

    def partition(left, right, pivot_index):
        pivot = arr[pivot_index]
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
        store_index = left
        for i in range(left, right):
            if arr[i] < pivot:
                arr[i], arr[store_index] = arr[store_index], arr[i]
                store_index += 1
        arr[right], arr[store_index] = arr[store_index], arr[right]
        return store_index

    def select(left, right, k_smallest):
        if left == right:
            return arr[left]

        pivot_index = left
        pivot_index = partition(left, right, pivot_index)

        if k_smallest == pivot_index + 1:
            return arr[pivot_index]
        elif k_smallest < pivot_index + 1:
            return select(left, pivot_index - 1, k_smallest)
        else:
            return select(pivot_index + 1, right, k_smallest)

    return select(0, len(arr) - 1, k)

def check(candidate):
    assert kth_element([12,3,5,7,19], 2) == 3
    assert kth_element([17,24,8,23], 3) == 8
    assert kth_element([16,21,25,36,4], 4) == 36

check(kth_element)