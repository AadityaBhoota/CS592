def noprofit_noloss(actual_cost, sale_amount): 
    return actual_cost == sale_amount

# Test the function with the given examples
assert noprofit_noloss(1500,1200) == False
assert noprofit_noloss(100,100) == True
assert noprofit_noloss(2000,5000) == False


def check(candidate):
    assert noprofit_noloss(1500,1200)==False
    assert noprofit_noloss(100,100)==True
    assert noprofit_noloss(2000,5000)==False

check(noprofit_noloss)