def fruit_distribution(s, n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of the fruits 
    in the basket, return the number of the mango fruits in the basket.
    
    Args:
    s (str): A string that represents the number of apples and oranges in the basket.
    n (int): The total number of fruits in the basket.
    
    Returns:
    int: The number of mango fruits in the basket.
    """
    # Split the string into the number of apples and oranges
    parts = s.split(" ")
    apples = int(parts[0])
    oranges = int(parts[-1])
    
    # Calculate the number of mango fruits
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