def car_race_collision(n: int) -> int:
    collisions = 0
    for i in range(-n + 1, n):
        left_to_right = i
        right_to_left = -i
        if left_to_right >= 0 and right_to_left < 0:
            collisions += 1
    return collisions



METADATA = {}


def check(candidate):
    assert candidate(2) == 4
    assert candidate(3) == 9
    assert candidate(4) == 16
    assert candidate(8) == 64
    assert candidate(10) == 100


check(car_race_collision)