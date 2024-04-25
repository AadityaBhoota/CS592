import math

def f(n):
    result = []  # Step 0: Create an empty list to store the output
    
    for i in range(1, n+1):  # Step 1: Run a loop from 1 to n (inclusive)
        if i % 2 == 0:  # Step 2: Check if the current index is even
            result.append(math.factorial(i))  # Step 3: Calculate the factorial of i and append it to the list
        else:
            result.append(sum(range(1, i+1)) )  # Step 5: Calculate the sum from 1 to i and append it to the list
    
    return result

def check(candidate):

    assert candidate(5) == [1, 2, 6, 24, 15]
    assert candidate(7) == [1, 2, 6, 24, 15, 720, 28]
    assert candidate(1) == [1]
    assert candidate(3) == [1, 2, 6]

check(f)