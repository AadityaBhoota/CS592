def fruit_distribution(s, n):
    apples = 0
    oranges = 0
    
    # Extract the number of apples and oranges from the input string
    for word in s.split():
        if word.isdigit():
            if "apple" in s:
                apples = int(word)
            elif "orange" in s:
                oranges = int(word)
    
    mangoes = n - apples - oranges
    return mangoes

# Test cases
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output should be 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output should be 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output should be 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output should be 19

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