def lps(s):
    n = len(s)
    # Create a table to store the lengths of palindromic subsequences
    dp = [[0 for _ in range(n)] for _ in range(n)]

    # Base case: single characters are palindromes of length 1
    for i in range(n):
        dp[i][i] = 1

    # Fill the table in a bottom-up manner
    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if s[i] == s[j] and cl == 2:
                dp[i][j] = 2
            elif s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

    return dp[0][n - 1]

# Test cases




def check(candidate):
    assert lps("TENS FOR TENS") == 5
    assert lps("CARDIO FOR CARDS") == 7
    assert lps("PART OF THE JOURNEY IS PART") == 9

check(lps)