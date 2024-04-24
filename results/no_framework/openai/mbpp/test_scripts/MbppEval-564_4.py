def count_Pairs(arr, n):
    unique_values = {}
    for num in arr:
        if num in unique_values:
            unique_values[num] += 1
        else:
            unique_values[num] = 1

    count_pairs = 0
    for value in unique_values.values():
        count_pairs += value * (n - value)

    return count_pairs // 2

# Testing the function with the provided examples




def check(candidate):
    assert count_Pairs([1,2,1],3) == 2
    assert count_Pairs([1,1,1,1],4) == 0
    assert count_Pairs([1,2,3,4,5],5) == 10

check(count_Pairs)