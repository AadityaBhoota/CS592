def lps(str):
    n = len(str)
    dp = [[0] * n for _ in range(n)]
    
    # Base cases
    for i in range(n):
        dp[i][i] = 1
    
    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if str[i] == str[j]:
                dp[i][j] = 2 + dp[i+1][j-1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    
    return dp[0][n-1]

def check(candidate):
    assert lps("TENS FOR TENS") == 5
    assert lps("CARDIO FOR CARDS") == 7
    assert lps("PART OF THE JOURNEY IS PART") == 9

check(lps)