def catalan_number(num):
    dp = [0] * (num + 1)
    dp[0] = 1
    for i in range(1, num + 1):
        for j in range(i):
            dp[i] += dp[j] * dp[i - j - 1]
    return dp[num]

def check(candidate):
    assert catalan_number(10)==16796
    assert catalan_number(9)==4862
    assert catalan_number(7)==429

check(catalan_number)