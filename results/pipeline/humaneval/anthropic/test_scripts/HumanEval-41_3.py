def car_race_collision(n: int) -> int:
    collision_count = 0
    for i in range(n):
        for j in range(n):
            if i != j:
                # Calculate the time when the cars collide
                collision_time = (i + j) / (i + j)
                # Check if the collision time is positive (i.e., the cars haven't passed each other yet)
                if collision_time > 0:
                    collision_count += 1
    return collision_count



METADATA = {}


def check(candidate):
    assert candidate(2) == 4
    assert candidate(3) == 9
    assert candidate(4) == 16
    assert candidate(8) == 64
    assert candidate(10) == 100


check(car_race_collision)