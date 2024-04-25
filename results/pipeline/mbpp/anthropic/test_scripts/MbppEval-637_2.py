def noprofit_noloss(actual_cost, sale_amount):
    profit_loss = sale_amount - actual_cost
    return profit_loss == 0

def check(candidate):
    assert noprofit_noloss(1500,1200)==False
    assert noprofit_noloss(100,100)==True
    assert noprofit_noloss(2000,5000)==False

check(noprofit_noloss)