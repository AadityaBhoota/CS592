def rearrange_bigger(n):
    digits = [int(d) for d in str(n)]  # Convert the number to a list of digits
    i = len(digits) - 2
    while i >= 0 and digits[i] >= digits[i + 1]:  
        i -= 1

    if i == -1:
        return False  # If no such index i exists, return False

    j = len(digits) - 1
    while digits[j] <= digits[i]:  
        j -= 1

    digits[i], digits[j] = digits[j], digits[i]  # Swap the digits at index i and index j
    digits[i+1:] = digits[i+1:][::-1]  # Reverse the digits from index i+1 till the end

    return int(''.join(map(str, digits)))  # Convert the list of digits back to a number and return it

def check(candidate):
    assert rearrange_bigger(12)==21
    assert rearrange_bigger(10)==False
    assert rearrange_bigger(102)==120

check(rearrange_bigger)