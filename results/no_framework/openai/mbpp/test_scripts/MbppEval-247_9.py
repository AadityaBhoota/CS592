def lps(s):
    n = len(s)
    L = [[0]*n for _ in range(n)]
    
    for i in range(n):
        L[i][i] = 1
    
    for cl in range(2, n+1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if s[i] == s[j] and cl == 2:
                L[i][j] = 2
            elif s[i] == s[j]:
                L[i][j] = L[i+1][j-1] + 2
            else:
                L[i][j] = max(L[i][j-1], L[i+1][j])
    
    return L[0][n-1]

# Test cases




def check(candidate):
    assert lps("TENS FOR TENS") == 5
    assert lps("CARDIO FOR CARDS") == 7
    assert lps("PART OF THE JOURNEY IS PART") == 9

check(lps)