def unique_Element(arr):
    unique_count = 0
    seen = set()
    for num in arr:
        if num not in seen:
            unique_count += 1
            seen.add(num)
    return 'YES' if unique_count == 1 else 'NO'

def check(candidate):
    assert unique_Element([1,1,1]) == True
    assert unique_Element([1,2,1,2]) == False
    assert unique_Element([1,2,3,4,5]) == False

check(unique_Element)