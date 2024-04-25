def get_max_triples(n):
    count = 0
    for i in range(1, n + 1):
        a_i = i * i - i + 1
        
        if a_i % 3 == 0:
            count += i - 1
    
    return count

# Test the function
n = 5


def check(candidate):

    assert candidate(5) == 1
    assert candidate(6) == 4
    assert candidate(10) == 36
    assert candidate(100) == 53361

check(get_max_triples)