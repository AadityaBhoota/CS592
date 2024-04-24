def eulerian_num(n, m):
    # Initialize a 2D list to store the Eulerian numbers
    eulerian = [[0 for j in range(m + 1)] for i in range(n + 1)]
    
    # Base case
    for i in range(m + 1):
        eulerian[0][i] = 1
    
    # Calculate Eulerian numbers using dynamic programming
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i >= j:
                eulerian[i][j] = (j + 1) * eulerian[i - 1][j] + (i - j) * eulerian[i - 1][j - 1]
    
    return eulerian[n][m]

# Test cases




def check(candidate):
    assert eulerian_num(3, 1) == 4
    assert eulerian_num(4, 1) == 11
    assert eulerian_num(5, 3) == 26

check(eulerian_num)