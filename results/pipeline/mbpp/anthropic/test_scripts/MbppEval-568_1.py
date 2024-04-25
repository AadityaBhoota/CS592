def empty_list(length):
    return [{} for _ in range(length)]

def check(candidate):
    assert empty_list(5)==[{},{},{},{},{}]
    assert empty_list(6)==[{},{},{},{},{},{}]
    assert empty_list(7)==[{},{},{},{},{},{},{}]

check(empty_list)