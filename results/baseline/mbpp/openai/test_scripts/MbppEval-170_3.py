def sum_range_list(list1, m, n):
    # Initialize the sum variable to store the total sum
    total_sum = 0
    
    # Iterate over the list and sum up the numbers within the range
    for number in list1:
        if m <= number <= n:
            total_sum += number
    
    return total_sum

# Test the function with the given examples




def check(candidate):
    assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10) == 29
    assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 5, 7) == 16
    assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 7, 10) == 38

check(sum_range_list)