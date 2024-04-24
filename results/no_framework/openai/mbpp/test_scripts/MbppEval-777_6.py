def find_sum(arr):
    distinct_elements = set()
    repeated_elements = set()
    total_sum = 0
    
    for num in arr:
        if num not in distinct_elements and num not in repeated_elements:
            distinct_elements.add(num)
            total_sum += num
        elif num in distinct_elements:
            distinct_elements.remove(num)
            repeated_elements.add(num)
            total_sum -= num
    
    return total_sum

# Test cases




def check(candidate):
    assert find_sum([1,2,3,1,1,4,5,6]) == 21
    assert find_sum([1,10,9,4,2,10,10,45,4]) == 71
    assert find_sum([12,10,9,45,2,10,10,45,10]) == 78

check(find_sum)