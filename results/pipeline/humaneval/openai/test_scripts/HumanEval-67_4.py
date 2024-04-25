def fruit_distribution(s, n):
    # Step 0: Extract the number of apples and oranges from the input string
    s = s.split()
    apples = int(s[0])
    oranges = int(s[3])

    # Step 1: Calculate the number of mango fruits by subtracting total apples and oranges from total fruits
    mangoes = n - apples - oranges
    return mangoes

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