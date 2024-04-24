def noprofit_noloss(actual_cost, sale_amount):
    """
    Write a function to check whether the given amount has no profit and no loss.

    Examples:
    noprofit_noloss(1500, 1200) == False
    noprofit_noloss(100, 100) == True
    noprofit_noloss(2000, 5000) == False
    """
    if actual_cost == sale_amount:
        return True
    else:
        return False

def check(candidate):
    assert noprofit_noloss(1500,1200)==False
    assert noprofit_noloss(100,100)==True
    assert noprofit_noloss(2000,5000)==False

check(noprofit_noloss)