def median_trapezium(base1, base2, height):
    median = (base1 + base2) / 2
    return median

# Test the function




def check(candidate):
    assert median_trapezium(15,25,35)==20
    assert median_trapezium(10,20,30)==15
    assert median_trapezium(6,9,4)==7.5

check(median_trapezium)