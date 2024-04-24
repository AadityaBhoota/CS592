def fruit_distribution(s, n):
    # Split the string into a list of words
    words = s.split()
    
    # Initialize the count of apples and oranges to 0
    apples = 0
    oranges = 0
    
    # Iterate through the list of words
    for i in range(len(words)):
        # Check if the current word is "apples"
        if words[i] == "apples":
            apples = int(words[i-1])
        # Check if the current word is "oranges"
        elif words[i] == "oranges":
            oranges = int(words[i-1])
    
    # Calculate the number of mangoes
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