def rearrange_bigger(n):
    num_list = list(str(n))
    for i in range(len(num_list) - 1, 0, -1):
        if num_list[i] > num_list[i - 1]:
            swap_index = i - 1
            break
    else:
        return False

    next_bigger = num_list[:swap_index]
    remaining = sorted(num_list[swap_index:])
    for i in range(len(remaining)):
        if remaining[i] > num_list[swap_index]:
            next_bigger.append(remaining[i])
            remaining[i] = num_list[swap_index]
            break

    next_bigger += remaining
    result = int(''.join(next_bigger))
    
    return result

# Testing the function with the provided examples




def check(candidate):
    assert rearrange_bigger(12)==21
    assert rearrange_bigger(10)==False
    assert rearrange_bigger(102)==120

check(rearrange_bigger)