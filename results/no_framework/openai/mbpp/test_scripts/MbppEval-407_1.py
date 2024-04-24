def rearrange_bigger(n):
    n = str(n)
    for i in range(len(n) - 1, 0, -1):
        if n[i] > n[i - 1]:
            pivot = n[i - 1]
            suffix = sorted(n[i:])
            for j in range(len(suffix)):
                if suffix[j] > pivot:
                    new_num = int(n[:i-1] + suffix[j] + ''.join(suffix[:j] + suffix[j+1:]))
                    return new_num
    return False

# Test cases




def check(candidate):
    assert rearrange_bigger(12)==21
    assert rearrange_bigger(10)==False
    assert rearrange_bigger(102)==120

check(rearrange_bigger)