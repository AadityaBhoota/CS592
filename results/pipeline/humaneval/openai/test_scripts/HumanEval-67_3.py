def fruit_distribution(s, n):
    apple_str = ''
    orange_str = ''
    for char in s:
        if char.isnumeric():
            if not orange_str:
                apple_str += char
            else:
                orange_str += char
    apples = int(apple_str)
    oranges = int(orange_str)
    
    mango = n - apples - oranges
    return mango

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