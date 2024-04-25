def triples_sum_to_zero(l: list):
    sorted_list = sorted(l)
    
    for i in range(len(sorted_list)):
        left = i + 1
        right = len(sorted_list) - 1
        
        while left < right:
            current_sum = sorted_list[i] + sorted_list[left] + sorted_list[right]
            if current_sum == 0:
                return True
            elif current_sum < 0:
                left += 1
            else:
                right -= 1
    
    return False



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