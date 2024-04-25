def remove_odd(l):
    even_nums = []
    for num in l:
        if num % 2 == 0:
            even_nums.append(num)
    return even_nums

def check(candidate):
    assert remove_odd([1,2,3]) == [2]
    assert remove_odd([2,4,6]) == [2,4,6]
    assert remove_odd([10,20,3]) == [10,20]

check(remove_odd)