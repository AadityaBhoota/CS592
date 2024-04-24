def count_Pairs(arr, n): 
    count = 0
    unique_elements = set(arr)
    
    for element in unique_elements:
        count += arr.count(element) * (n - arr.count(element))

    return count // 2  # Since pairs are unordered, divide by 2 to avoid double counting

# Test cases




def check(candidate):
    assert count_Pairs([1,2,1],3) == 2
    assert count_Pairs([1,1,1,1],4) == 0
    assert count_Pairs([1,2,3,4,5],5) == 10

check(count_Pairs)