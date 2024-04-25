def catalan_number(num):
    if num < 0:
        return "Please provide a non-negative number for calculating Catalan number."

    if num == 0:
        return 1
    else:
        c = [0] * (num+1)
        c[0] = 1

        def calculate_catalan(n):
            if c[n] != 0:
                return c[n]

            res = 0
            for i in range(n):
                res += calculate_catalan(i) * calculate_catalan(n - i - 1)
            c[n] = res
            return res

        return calculate_catalan(num)

def check(candidate):
    assert catalan_number(10)==16796
    assert catalan_number(9)==4862
    assert catalan_number(7)==429

check(catalan_number)