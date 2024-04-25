def fruit_distribution(s, n):
    nums = [int(word) for word in s.split() if word.isdigit()]
    apples = nums[0] if "apples" in s else 0
    oranges = nums[1] if "oranges" in s else 0
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