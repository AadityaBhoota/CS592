def fruit_distribution(s, n):
    words = s.split()
    apples_index = words.index("apples")
    oranges_index = words.index("oranges")
    num_apples = int(words[apples_index - 1])
    num_oranges = int(words[oranges_index - 1])
    num_mangoes = n - num_apples - num_oranges
    return num_mangoes

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