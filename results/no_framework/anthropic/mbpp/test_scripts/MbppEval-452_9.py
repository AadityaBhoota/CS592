def loss_amount(actual_cost, sale_amount):
    """
    Write a function that gives loss amount on a sale if the given amount has loss else return 0.

    Examples:
    loss_amount(1500, 1200) == 300
    loss_amount(100, 200) == 0
    loss_amount(2000, 5000) == 0
    """
    if actual_cost > sale_amount:
        return actual_cost - sale_amount
    else:
        return 0

def check(candidate):
    assert loss_amount(1500,1200)==0
    assert loss_amount(100,200)==100
    assert loss_amount(2000,5000)==3000

check(loss_amount)