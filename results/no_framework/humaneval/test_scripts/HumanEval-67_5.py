def fruit_distribution(s, n):
    # Extract the number of apples and oranges from the input string
    apples_str, oranges_str = s.split(" and ")
    apples = int(apples_str.split()[0])
    oranges = int(oranges_str.split()[0])
    
    # Calculate the number of mango fruits in the basket
    mango = n - apples - oranges
    
    return mango

# Test the function with the provided examples





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