def find_sum(arr, n):
    # Count the occurrences of each element in the list
    count_dict = {}
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    # Sum up the non-repeating elements
    result = 0
    for key, value in count_dict.items():
        if value == 1:
            result += key

    return result

# Examples




def check(candidate):
    assert find_sum([1,2,3,1,1,4,5,6]) == 21
    assert find_sum([1,10,9,4,2,10,10,45,4]) == 71
    assert find_sum([12,10,9,45,2,10,10,45,10]) == 78

check(find_sum)