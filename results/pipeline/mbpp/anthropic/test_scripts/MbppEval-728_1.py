def sum_list(lst1, lst2):
    if not lst1 or not lst2:
        return []

    max_length = max(len(lst1), len(lst2))
    lst1 = lst1 + [0] * (max_length - len(lst1))
    lst2 = lst2 + [0] * (max_length - len(lst2))

    return [a + b for a, b in zip(lst1, lst2)]

def check(candidate):
    assert sum_list([10,20,30],[15,25,35])==[25,45,65]
    assert sum_list([1,2,3],[5,6,7])==[6,8,10]
    assert sum_list([15,20,30],[15,45,75])==[30,65,105]

check(sum_list)