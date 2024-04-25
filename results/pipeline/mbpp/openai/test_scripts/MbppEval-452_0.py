def loss_amount(actual_cost, sale_amount):
    profit_loss = sale_amount - actual_cost
    
    if profit_loss < 0:  # Check for loss
        return abs(profit_loss)
    else:  # No loss
        return 0

def check(candidate):
    assert loss_amount(1500,1200)==0
    assert loss_amount(100,200)==100
    assert loss_amount(2000,5000)==3000

check(loss_amount)