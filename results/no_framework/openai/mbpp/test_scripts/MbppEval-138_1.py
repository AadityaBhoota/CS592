def is_Sum_Of_Powers_Of_Two(n):
    # If n is already a power of 2, return True
    if n & (n-1) == 0 and n > 0:
        return True

    # Try to find a subset of powers of 2 that sum up to n
    powers = [1]
    while powers[-1] * 2 <= n:
        powers.append(powers[-1] * 2)
    
    k = len(powers)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(k):
        for j in range(n, powers[i]-1, -1):
            dp[j] = dp[j] or dp[j - powers[i]]
    
    return dp[n]

# Test cases




def check(candidate):
    assert is_Sum_Of_Powers_Of_Two(10) == True
    assert is_Sum_Of_Powers_Of_Two(7) == False
    assert is_Sum_Of_Powers_Of_Two(14) == True

check(is_Sum_Of_Powers_Of_Two)