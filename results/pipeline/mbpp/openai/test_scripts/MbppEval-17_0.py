# Step 0: Define the function square_perimeter(a)
def square_perimeter(a):
    # Step 1: Calculate the perimeter of the square
    perimeter = 4 * a
    return perimeter

# Test cases




def check(candidate):
    assert square_perimeter(10)==40
    assert square_perimeter(5)==20
    assert square_perimeter(4)==16

check(square_perimeter)