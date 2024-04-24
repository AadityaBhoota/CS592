def car_race_collision(n: int):
    """
    Calculate the total number of collisions that occur when n cars moving left to right
    overtake n cars moving right to left.

    Args:
    n (int): The number of cars moving in each direction.

    Returns:
    int: The total number of collisions.
    """
    return n**2



METADATA = {}


def check(candidate):
    assert candidate(2) == 4
    assert candidate(3) == 9
    assert candidate(4) == 16
    assert candidate(8) == 64
    assert candidate(10) == 100


check(car_race_collision)