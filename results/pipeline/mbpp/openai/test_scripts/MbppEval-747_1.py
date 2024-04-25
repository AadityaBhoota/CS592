def lcs_of_three(X, Y, Z): 
    m, n, o = len(X), len(Y), len(Z)
    
    lcs = [[[0 for _ in range(o + 1)] for _ in range(n + 1)] for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            for k in range(1, o + 1):
                if X[i-1] == Y[j-1] == Z[k-1]:
                    lcs[i][j][k] = lcs[i-1][j-1][k-1] + 1
                else:
                    lcs[i][j][k] = max(lcs[i-1][j][k], lcs[i][j-1][k], lcs[i][j][k-1])
    
    return lcs[m][n][o]

def check(candidate):
    assert lcs_of_three('AGGT12', '12TXAYB', '12XBA') == 2
    assert lcs_of_three('Reels', 'Reelsfor', 'ReelsforReels') == 5
    assert lcs_of_three('abcd1e2', 'bc12ea', 'bd1ea') == 3

check(lcs_of_three)