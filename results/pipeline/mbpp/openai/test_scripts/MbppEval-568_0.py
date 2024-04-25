def empty_list(length):
    result = []
    empty_dict = {}
    for _ in range(length):
        result.append(empty_dict.copy())
    return result

def check(candidate):
    assert empty_list(5)==[{},{},{},{},{}]
    assert empty_list(6)==[{},{},{},{},{},{}]
    assert empty_list(7)==[{},{},{},{},{},{},{}]

check(empty_list)