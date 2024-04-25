def find_sum(arr):
    freq_dict = {}  # Step 0: Create a dictionary to store the frequency of each element
    
    for num in arr:  # Step 1: Count the frequency of each element in the dictionary
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    
    non_repeated_sum = sum(key for key, value in freq_dict.items() if value == 1)  # Step 2: Summing non-repeated elements
    
    return non_repeated_sum

def check(candidate):
    assert find_sum([1,2,3,1,1,4,5,6]) == 21
    assert find_sum([1,10,9,4,2,10,10,45,4]) == 71
    assert find_sum([12,10,9,45,2,10,10,45,10]) == 78

check(find_sum)