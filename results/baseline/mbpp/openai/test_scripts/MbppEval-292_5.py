def find(n, m):
    return n // m

# Testing the function




def check(candidate):
    assert find(10,3) == 3
    assert find(4,2) == 2
    assert find(20,5) == 4

check(find)