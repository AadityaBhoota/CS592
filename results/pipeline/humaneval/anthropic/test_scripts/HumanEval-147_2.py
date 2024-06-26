def get_max_triples(n):
    a = [i * i - i + 1 for i in range(1, n+1)]
    count = 0
    
    for i in range(n):
        if a[i] % 3 == 0:
            for j in range(i+1, n):
                if (a[j] + a[i]) % 3 == 0:
                    count += 1
    
    return count

def check(candidate):

    assert candidate(5) == 1
    assert candidate(6) == 4
    assert candidate(10) == 36
    assert candidate(100) == 53361

check(get_max_triples)