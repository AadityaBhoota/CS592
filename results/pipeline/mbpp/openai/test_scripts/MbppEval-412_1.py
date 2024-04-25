def remove_odd(l):
    result = []

    for num in l:
        if num % 2 == 0:  # Check if the number is even
            result.append(num)  # If the number is even, add it to the result list
    
    return result

def check(candidate):
    assert remove_odd([1,2,3]) == [2]
    assert remove_odd([2,4,6]) == [2,4,6]
    assert remove_odd([10,20,3]) == [10,20]

check(remove_odd)