def loss_amount(actual_cost, sale_amount):
    if actual_cost > sale_amount:
        return actual_cost - sale_amount
    else:
        return 0

assert loss_amount(1500, 1200) == None
assert loss_amount(100, 200) == 100
assert loss_amount(2000, 5000) == 3000

def check(candidate):
    assert loss_amount(1500,1200)==0
    assert loss_amount(100,200)==100
    assert loss_amount(2000,5000)==3000

check(loss_amount)