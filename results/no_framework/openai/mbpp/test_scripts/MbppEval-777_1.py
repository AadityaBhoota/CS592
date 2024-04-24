def find_sum(arr, n):
    unique_elements = set()
    total_sum = 0

    for number in arr:
        if arr.count(number) == 1:
            unique_elements.add(number)

    total_sum = sum(unique_elements)

    return total_sum

# Test cases




def check(candidate):
    assert find_sum([1,2,3,1,1,4,5,6]) == 21
    assert find_sum([1,10,9,4,2,10,10,45,4]) == 71
    assert find_sum([12,10,9,45,2,10,10,45,10]) == 78

check(find_sum)