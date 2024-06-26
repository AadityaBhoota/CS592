def bell_Number(n): 
    if n < 0:
        return -1
    
    bell = [[0 for _ in range(n+1)] for _ in range(n+1)]
    bell[0][0] = 1
    
    for i in range(1, n+1):
        bell[i][0] = bell[i-1][i-1]
        for j in range(1, i+1):
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]

    return bell[n][n]

def check(candidate):
    assert bell_Number(2) == 2
    assert bell_Number(3) == 5
    assert bell_Number(4) == 15

check(bell_Number)