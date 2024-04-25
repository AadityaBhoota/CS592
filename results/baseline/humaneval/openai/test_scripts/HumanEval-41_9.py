def car_race_collision(n: int):
    # Calculate the number of collisions using the sum of n natural numbers formula
    total_collisions = (n - 1) * n // 2
    return total_collisions

# Test the function with n = 5
n = 5




METADATA = {}


def check(candidate):
    assert candidate(2) == 4
    assert candidate(3) == 9
    assert candidate(4) == 16
    assert candidate(8) == 64
    assert candidate(10) == 100


check(car_race_collision)