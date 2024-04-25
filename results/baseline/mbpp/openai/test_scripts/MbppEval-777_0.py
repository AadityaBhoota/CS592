def find_sum(arr):
    unique_elements = set()
    sum_of_unique_elements = 0
    
    for num in arr:
        if arr.count(num) == 1:  # Count of an element in the list should be 1 for it to be non-repeated
            unique_elements.add(num)
    
    for unique_num in unique_elements:
        sum_of_unique_elements += unique_num
    
    return sum_of_unique_elements

# Test cases




def check(candidate):
    assert find_sum([1,2,3,1,1,4,5,6]) == 21
    assert find_sum([1,10,9,4,2,10,10,45,4]) == 71
    assert find_sum([12,10,9,45,2,10,10,45,10]) == 78

check(find_sum)