def division_elements(test_tup1, test_tup2):
    results = []
    for i in range(len(test_tup1)):
        result = test_tup1[i] / test_tup2[i]
        results.append(result)
    return tuple(results)

def check(candidate):
    assert division_elements((10, 4, 6, 9),(5, 2, 3, 3)) == (2, 2, 2, 3)
    assert division_elements((12, 6, 8, 16),(6, 3, 4, 4)) == (2, 2, 2, 4)
    assert division_elements((20, 14, 36, 18),(5, 7, 6, 9)) == (4, 2, 6, 2)

check(division_elements)