def lps(str):
    n = len(str)
    dp = [[0] * n for _ in range(n)]

    # Base case: for substrings of length 1, the length of the longest palindromic subsequence is 1
    for i in range(n):
        dp[i][i] = 1

    # For substrings of length 2, if the characters are the same, the length is 2, else it is 1
    for i in range(n-1):
        if str[i] == str[i+1]:
            dp[i][i+1] = 2
        else:
            dp[i][i+1] = 1

    # For substrings of length greater than 2
    for length in range(3, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if str[i] == str[j]:
                dp[i][j] = 2 + dp[i+1][j-1]
            else:
                dp[i][j] = max(dp[i][j-1], dp[i+1][j])

    return dp[0][n-1]

def check(candidate):
    assert lps("TENS FOR TENS") == 5
    assert lps("CARDIO FOR CARDS") == 7
    assert lps("PART OF THE JOURNEY IS PART") == 9

check(lps)