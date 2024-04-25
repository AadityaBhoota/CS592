def loss_amount(actual_cost, sale_amount):
    if sale_amount < actual_cost:
        return actual_cost - sale_amount
    else:
        return 0

def check(candidate):
    assert loss_amount(1500,1200)==0
    assert loss_amount(100,200)==100
    assert loss_amount(2000,5000)==3000

check(loss_amount)