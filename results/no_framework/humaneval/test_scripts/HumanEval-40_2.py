def triples_sum_to_zero(l: list):
    n = len(l)
    if n < 3:
        return False
    
    l.sort()
    for i in range(n-2):
        if i == 0 or l[i] > l[i-1]:
            left = i + 1
            right = n - 1
            while left < right:
                total = l[i] + l[left] + l[right]
                if total == 0:
                    return True
                elif total < 0:
                    left += 1
                else:
                    right -= 1
                
    return False

# Run the test cases
if __name__ == "__main__":
    import doctest
    doctest.testmod()



METADATA = {}


def check(candidate):
    assert candidate([1, 3, 5, 0]) == False
    assert candidate([1, 3, 5, -1]) == False
    assert candidate([1, 3, -2, 1]) == True
    assert candidate([1, 2, 3, 7]) == False
    assert candidate([1, 2, 5, 7]) == False
    assert candidate([2, 4, -5, 3, 9, 7]) == True
    assert candidate([1]) == False
    assert candidate([1, 3, 5, -100]) == False
    assert candidate([100, 3, 5, -100]) == False


check(triples_sum_to_zero)