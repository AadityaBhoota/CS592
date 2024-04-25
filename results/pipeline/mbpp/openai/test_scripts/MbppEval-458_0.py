def rectangle_area(l, b):
    # Step 1: Define the function rectangle_area with parameters l and b
    area = l * b  # Step 2: Calculate the area of the rectangle
    return area  # Step 3: Return the calculated area

def check(candidate):
    assert rectangle_area(10,20)==200
    assert rectangle_area(10,5)==50
    assert rectangle_area(4,2)==8

check(rectangle_area)