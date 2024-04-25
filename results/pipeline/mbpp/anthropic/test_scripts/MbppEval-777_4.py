def find_sum(arr):
    sum_of_unique = 0
    unique_elements = set()
    
    for num in arr:
        if num not in unique_elements:
            unique_elements.add(num)
            sum_of_unique += num
    
    return sum_of_unique

def check(candidate):
    assert find_sum([1,2,3,1,1,4,5,6]) == 21
    assert find_sum([1,10,9,4,2,10,10,45,4]) == 71
    assert find_sum([12,10,9,45,2,10,10,45,10]) == 78

check(find_sum)