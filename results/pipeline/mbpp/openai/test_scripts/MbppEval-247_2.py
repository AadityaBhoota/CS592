def lps(s):
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        dp[i][i] = 1
    
    for end in range(1, n):
        for start in range(end - 1, -1, -1):
            if s[start] == s[end]:
                dp[start][end] = dp[start + 1][end - 1] + 2
            else:
                dp[start][end] = max(dp[start + 1][end], dp[start][end - 1])
    
    return dp[0][-1]

def check(candidate):
    assert lps("TENS FOR TENS") == 5
    assert lps("CARDIO FOR CARDS") == 7
    assert lps("PART OF THE JOURNEY IS PART") == 9

check(lps)