def count_Pairs(arr, n):
    '''
    Count the number of possible unordered pairs where both elements are unequal.

    :param arr: List of integers
    :param n: Length of the list
    :return: Number of possible unordered pairs
    '''
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] != arr[j]:
                count += 1
    return count

# Testing the function with provided examples




def check(candidate):
    assert count_Pairs([1,2,1],3) == 2
    assert count_Pairs([1,1,1,1],4) == 0
    assert count_Pairs([1,2,3,4,5],5) == 10

check(count_Pairs)