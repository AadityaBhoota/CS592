def fruit_distribution(s, n):
    parts = s.split()
    apples = 0
    oranges = 0
    
    for i in range(0, len(parts), 2):
        if parts[i] == 'apples':
            apples = int(parts[i-1])
        elif parts[i] == 'oranges':
            oranges = int(parts[i-1])

    mango = n - apples - oranges
    return mango

# Test the function with some sample inputs





def check(candidate):

    # Check some simple cases
    assert candidate("5 apples and 6 oranges",19) == 8
    assert candidate("5 apples and 6 oranges",21) == 10
    assert candidate("0 apples and 1 oranges",3) == 2
    assert candidate("1 apples and 0 oranges",3) == 2
    assert candidate("2 apples and 3 oranges",100) == 95
    assert candidate("2 apples and 3 oranges",5) == 0
    assert candidate("1 apples and 100 oranges",120) == 19

check(fruit_distribution)