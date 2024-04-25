def noprofit_noloss(actual_cost, sale_amount):
    difference = sale_amount - actual_cost
    return difference == 0

def check(candidate):
    assert noprofit_noloss(1500,1200)==False
    assert noprofit_noloss(100,100)==True
    assert noprofit_noloss(2000,5000)==False

check(noprofit_noloss)