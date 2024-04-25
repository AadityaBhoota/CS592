def median_trapezium(base1, base2, height):
    # Step 0: Calculate the sum of the two bases
    bases_sum = base1 + base2
    
    # Step 1: Calculate the average of the bases
    median = bases_sum / 2
    
    # Step 2: Return the average as the median length of the trapezium
    return median

def check(candidate):
    assert median_trapezium(15,25,35)==20
    assert median_trapezium(10,20,30)==15
    assert median_trapezium(6,9,4)==7.5

check(median_trapezium)