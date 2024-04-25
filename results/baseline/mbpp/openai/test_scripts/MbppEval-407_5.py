def rearrange_bigger(n):
    num_list = list(str(n))

    for i in range(len(num_list)-1, 0, -1):
        if num_list[i] > num_list[i-1]:
            min_index = i
            for j in range(i, len(num_list)):
                if num_list[j] > num_list[i-1] and num_list[j] < num_list[min_index]:
                    min_index = j
            
            num_list[i-1], num_list[min_index] = num_list[min_index], num_list[i-1]
            num_list[i:] = sorted(num_list[i:])
            next_bigger = int("".join(num_list))
            return next_bigger

    return False

# Test cases




def check(candidate):
    assert rearrange_bigger(12)==21
    assert rearrange_bigger(10)==False
    assert rearrange_bigger(102)==120

check(rearrange_bigger)