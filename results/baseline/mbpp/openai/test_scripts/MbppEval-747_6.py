def lcs_of_three(X, Y, Z, m, n, o):
    L = [[[0 for _ in range(o+1)] for _ in range(n+1)] for _ in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            for k in range(o+1):
                if i == 0 or j == 0 or k == 0:
                    L[i][j][k] = 0
                elif X[i-1] == Y[j-1] and X[i-1] == Z[k-1]:
                    L[i][j][k] = L[i-1][j-1][k-1] + 1
                else:
                    L[i][j][k] = max(L[i-1][j][k], L[i][j-1][k], L[i][j][k-1])

    return L[m][n][o]

# Test cases




def check(candidate):
    assert lcs_of_three('AGGT12', '12TXAYB', '12XBA') == 2
    assert lcs_of_three('Reels', 'Reelsfor', 'ReelsforReels') == 5
    assert lcs_of_three('abcd1e2', 'bc12ea', 'bd1ea') == 3

check(lcs_of_three)