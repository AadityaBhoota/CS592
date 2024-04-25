def car_race_collision(n: int):
    collision_count = 0

    for i in range(1, n + 1):
        collision_count += i
        
    return collision_count



METADATA = {}


def check(candidate):
    assert candidate(2) == 4
    assert candidate(3) == 9
    assert candidate(4) == 16
    assert candidate(8) == 64
    assert candidate(10) == 100


check(car_race_collision)