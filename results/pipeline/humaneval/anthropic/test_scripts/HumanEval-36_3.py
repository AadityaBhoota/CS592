def fizz_buzz(n: int) -> int:
    count = 0
    for i in range(11, n, 11):
        if '7' in str(i) or any('7' in str(j) for j in range(i, n, i)):
            count += 1
    for i in range(13, n, 13):
        if '7' in str(i) or any('7' in str(j) for j in range(i, n, i)):
            count += 1
    return count



METADATA = {}


def check(candidate):
    assert candidate(50) == 0
    assert candidate(78) == 2
    assert candidate(79) == 3
    assert candidate(100) == 3
    assert candidate(200) == 6
    assert candidate(4000) == 192
    assert candidate(10000) == 639
    assert candidate(100000) == 8026


check(fizz_buzz)