def car_race_collision(n: int):
    left_to_right = [i for i in range(n)]  # Initialize positions of cars moving left to right
    right_to_left = [i for i in range(2 * n - 1, n - 1, -1)]  # Initialize positions of cars moving right to left
    collisions = 0  # Initialize collision counter

    for pos_lr, pos_rl in zip(left_to_right, right_to_left):
        if pos_lr >= pos_rl:  # Check for overlap of car positions
            collisions += 1  # Increment collision counter if a collision occurs

    return collisions  # Return the total number of collisions



METADATA = {}


def check(candidate):
    assert candidate(2) == 4
    assert candidate(3) == 9
    assert candidate(4) == 16
    assert candidate(8) == 64
    assert candidate(10) == 100


check(car_race_collision)