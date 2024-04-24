def lps(string):
    """
    Find the length of the longest palindromic subsequence in the given string.

    Args:
        string (str): The input string.

    Returns:
        int: The length of the longest palindromic subsequence.
    """
    n = len(string)
    dp = [[0] * n for _ in range(n)]

    # Fill the diagonal elements
    for i in range(n):
        dp[i][i] = 1

    # Fill the remaining elements
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if string[i] == string[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]

def check(candidate):
    assert lps("TENS FOR TENS") == 5
    assert lps("CARDIO FOR CARDS") == 7
    assert lps("PART OF THE JOURNEY IS PART") == 9

check(lps)