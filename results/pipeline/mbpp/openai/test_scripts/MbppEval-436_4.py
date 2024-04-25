def neg_nos(list1):
    neg_nums = []

    for num in list1:
        if num < 0:
            neg_nums.append(num)

    return neg_nums

def check(candidate):
    assert neg_nos([-1,4,5,-6]) == [-1,-6]
    assert neg_nos([-1,-2,3,4]) == [-1,-2]
    assert neg_nos([-7,-6,8,9]) == [-7,-6]

check(neg_nos)