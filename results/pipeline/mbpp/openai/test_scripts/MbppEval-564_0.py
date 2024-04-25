def count_Pairs(arr, n):
    count = 0
    
    for i in range(n):  # Loop through each element in the list
        for j in range(i + 1, n):  # Iterate over the remaining elements
            if arr[i] != arr[j]:  # Check if the elements are unequal
                count += 1  # Increment count by 1
                
    return count  # Return the final count

def check(candidate):
    assert count_Pairs([1,2,1],3) == 2
    assert count_Pairs([1,1,1,1],4) == 0
    assert count_Pairs([1,2,3,4,5],5) == 10

check(count_Pairs)