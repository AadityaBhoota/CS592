def catalan_number(num):
    if num == 0:
        return 1

    catalan = 1
    for i in range(num):
        catalan = catalan * 2 * (2 * i + 1) // (i + 2)

    return catalan

# Test cases




def check(candidate):
    assert catalan_number(10)==16796
    assert catalan_number(9)==4862
    assert catalan_number(7)==429

check(catalan_number)