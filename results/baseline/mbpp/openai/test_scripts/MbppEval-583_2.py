def catalan_number(num):
    if num == 0:
        return 1
    else:
        res = [0] * (num + 1)
        res[0], res[1] = 1, 1

        for i in range(2, num + 1):
            for j in range(i):
                res[i] += res[j] * res[i - j - 1]

        return res[num]

# Test the function with the given examples




def check(candidate):
    assert catalan_number(10)==16796
    assert catalan_number(9)==4862
    assert catalan_number(7)==429

check(catalan_number)