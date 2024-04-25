def lps(str):
    n = len(str)
    dp = [[0] * n for _ in range(n)]
    
    # Initialize the diagonal elements
    for i in range(n):
        dp[i][i] = 1
    
    # Fill the dp table
    for length in range(2, n+1):
        for start in range(n - length + 1):
            end = start + length - 1
            if str[start] == str[end]:
                dp[start][end] = dp[start+1][end-1] + 2
            else:
                dp[start][end] = max(dp[start+1][end], dp[start][end-1])
    
    return dp[0][n-1]

def check(candidate):
    assert lps("TENS FOR TENS") == 5
    assert lps("CARDIO FOR CARDS") == 7
    assert lps("PART OF THE JOURNEY IS PART") == 9

check(lps)