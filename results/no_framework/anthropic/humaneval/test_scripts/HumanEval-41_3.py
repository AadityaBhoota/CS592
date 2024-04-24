def car_race_collision(n: int) -> int:
    """
    Calculates the number of collisions between cars moving in opposite directions.
    
    Args:
        n (int): The number of cars moving in each direction.
        
    Returns:
        int: The number of collisions.
    """
    return n * (n - 1) // 2



METADATA = {}


def check(candidate):
    assert candidate(2) == 4
    assert candidate(3) == 9
    assert candidate(4) == 16
    assert candidate(8) == 64
    assert candidate(10) == 100


check(car_race_collision)