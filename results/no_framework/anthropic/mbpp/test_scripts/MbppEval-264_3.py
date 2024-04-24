def dog_age(h_age):
    """
    Calculates a dog's age in dog years.

    Args:
        h_age (int): The human age of the dog.

    Returns:
        int: The dog's age in dog years.
    """
    if h_age <= 2:
        return h_age * 10.5
    else:
        return 21 + (h_age - 2) * 4

# Examples:




def check(candidate):
    assert dog_age(12)==61
    assert dog_age(15)==73
    assert dog_age(24)==109

check(dog_age)