from itertools import combinations

def find_combinations(test_list):
    """
    Write a function to find the combinations of sums with tuples in the given tuple list.
    """
    result = set()
    for combo in combinations(test_list, 2):
        result.add((sum(combo[0]), sum(combo[1])))
        result.add((sum(combo[1]), sum(combo[0])))
    return list(result)

def check(candidate):
    assert find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]) == [(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11)]
    assert find_combinations([(3, 5), (7, 8), (6, 2), (7, 11)]) == [(10, 13), (9, 7), (10, 16), (13, 10), (14, 19), (13, 13)]
    assert find_combinations([(4, 6), (8, 9), (7, 3), (8, 12)]) == [(12, 15), (11, 9), (12, 18), (15, 12), (16, 21), (15, 15)]

check(find_combinations)