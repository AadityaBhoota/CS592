def fruit_distribution(s, n):
    # Split the input string based on spaces
    fruits = s.split()
    
    # Initialize variables for apples, oranges, and mangoes
    apples = 0
    oranges = 0
    
    # Parse the input string to extract the number of apples and oranges
    for i in range(len(fruits)):
        if fruits[i] == 'apples':
            apples = int(fruits[i-1])
        elif fruits[i] == 'oranges':
            oranges = int(fruits[i-1])
    
    # Calculate the number of mangoes in the basket
    mangoes = n - apples - oranges
    
    return mangoes

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