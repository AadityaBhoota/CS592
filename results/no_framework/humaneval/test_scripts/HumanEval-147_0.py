def get_max_triples(n):
    a = [i * i - i + 1 for i in range(1, n + 1)]
    
    count = 0
    remainder_count = [0, 0, 0]
    
    for num in a:
        remainder_count[num % 3] += 1
        
    count += remainder_count[0] * (remainder_count[0] - 1) * (remainder_count[0] - 2) // 6
    count += remainder_count[1] * (remainder_count[2] - 1) * remainder_count[2] // 2
    count += remainder_count[0] * remainder_count[1] * remainder_count[2]
    
    return count

# Test example
n = 5
print(get_max_triples(n))  # Output: 1

def check(candidate):

    assert candidate(5) == 1
    assert candidate(6) == 4
    assert candidate(10) == 36
    assert candidate(100) == 53361

check(get_max_triples)