def car_race_collision(n: int):
    return min(n, n-1)

# Test the function with some cases
print(car_race_collision(3))  # Output: 2
print(car_race_collision(5))  # Output: 4
print(car_race_collision(1))  # Output: 0
print(car_race_collision(0))  # Output: 0



METADATA = {}


def check(candidate):
    assert candidate(2) == 4
    assert candidate(3) == 9
    assert candidate(4) == 16
    assert candidate(8) == 64
    assert candidate(10) == 100


check(car_race_collision)