def car_race_collision(n: int) -> int:
    total_collisions = 0
    for i in range(n):
        time_to_center = i / 2
        collisions_at_center = n - int(time_to_center)
        total_collisions += collisions_at_center
    return total_collisions



METADATA = {}


def check(candidate):
    assert candidate(2) == 4
    assert candidate(3) == 9
    assert candidate(4) == 16
    assert candidate(8) == 64
    assert candidate(10) == 100


check(car_race_collision)