def fruit_distribution(s, n):
    # Split the input string into separate words
    words = s.split()
    
    # Initialize variables to hold the count of apples and oranges
    apples = 0
    oranges = 0
    
    # Loop through the words to find the count of apples and oranges
    for i in range(len(words)):
        if words[i] == 'apples':
            apples = int(words[i-1])
        elif words[i] == 'oranges':
            oranges = int(words[i-1])
    
    # Calculate the count of mangoes
    mangoes = n - apples - oranges
    
    return mangoes

# Test cases
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19

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