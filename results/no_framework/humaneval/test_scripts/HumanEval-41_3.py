def car_race_collision(n: int):
    total_collisions = (n * n) // 2
    return total_collisions

# Test the function with an example
n = 3
print(car_race_collision(n))  # Output: 4



METADATA = {}


def check(candidate):
    assert candidate(2) == 4
    assert candidate(3) == 9
    assert candidate(4) == 16
    assert candidate(8) == 64
    assert candidate(10) == 100


check(car_race_collision)