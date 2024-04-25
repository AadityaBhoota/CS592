def fizz_buzz(n: int):
    count = 0  # Step 0
    
    for num in range(1, n):  # Step 1
        if num % 11 == 0 or num % 13 == 0:  # Step 2
            if '7' in str(num):  # Step 3
                count += 1  # Step 4
    
    return count  # Step 6



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