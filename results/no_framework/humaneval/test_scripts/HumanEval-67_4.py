def fruit_distribution(s, n):
    # Split the string into individual words
    words = s.split()
    
    # Extract the numbers of apples and oranges from the string
    apples = int(words[0]) if words[0].isdigit() else 0
    oranges = int(words[-2]) if words[-2].isdigit() else 0
    
    # Calculate the number of mango fruits
    mango = n - apples - oranges
    
    return mango

# Test cases





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