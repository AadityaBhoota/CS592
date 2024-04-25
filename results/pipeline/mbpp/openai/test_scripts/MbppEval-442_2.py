from array import array

def positive_count(nums):
    positive_nums_count = 0  # Step 0: Initialize a variable to count positive numbers
    
    # Step 1: Iterate through each number in nums
    for num in nums:
        if num > 0:
            positive_nums_count += 1  # Step 2: Count positive numbers
    
    ratio = positive_nums_count / len(nums)  # Step 3: Calculate ratio of positive numbers
    
    return round(ratio, 2)  # Step 4: Return the ratio rounded to 2 decimal places

def check(candidate):
    assert positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])==0.54
    assert positive_count([2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8])==0.69
    assert positive_count([2, 4, -6, -9, 11, -12, 14, -5, 17])==0.56

check(positive_count)