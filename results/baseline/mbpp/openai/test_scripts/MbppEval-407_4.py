def rearrange_bigger(n):
    num_list = list(str(n))

    for i in range(len(num_list) - 1, 0, -1):
        if num_list[i] > num_list[i - 1]:
            pivot = num_list[i - 1]
            suffix = num_list[i:]
            min_suffix = min([x for x in suffix if x > pivot])
            suffix.remove(min_suffix)
            suffix.sort()
            new_num = int("".join(num_list[:i-1] + [min_suffix] + suffix))
            return new_num

    return False

def check(candidate):
    assert rearrange_bigger(12)==21
    assert rearrange_bigger(10)==False
    assert rearrange_bigger(102)==120

check(rearrange_bigger)