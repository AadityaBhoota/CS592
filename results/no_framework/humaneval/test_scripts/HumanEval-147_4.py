def get_max_triples(n):
    a = [(i * i - i + 1) for i in range(1, n + 1)]
    count = 0
    remainder_count = {0: 0, 1: 0, 2: 0}
    
    for i in a:
        remainder_count[i % 3] += 1

    count += remainder_count[0] * (remainder_count[0] - 1) * (remainder_count[0] - 2) // 6
    count += remainder_count[1] * remainder_count[2] * remainder_count[0]
    count += remainder_count[2] * (remainder_count[2] - 1) * (remainder_count[2] - 2) // 6
    
    return count


# Test the function with the example input
n = 5


def check(candidate):

    assert candidate(5) == 1
    assert candidate(6) == 4
    assert candidate(10) == 36
    assert candidate(100) == 53361

check(get_max_triples)