def catalan_number(num):
    if num == 0:
        return 1
    else:
        result = 0
        for i in range(num):
            result += catalan_number(i) * catalan_number(num-1-i)
        return result

# Testing the function




def check(candidate):
    assert catalan_number(10)==16796
    assert catalan_number(9)==4862
    assert catalan_number(7)==429

check(catalan_number)