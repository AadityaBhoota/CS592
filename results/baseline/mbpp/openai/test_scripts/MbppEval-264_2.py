def dog_age(h_age):
    if h_age <= 0:
        return "Invalid age input. Age must be a positive number."

    if h_age <= 2:
        dog_years = h_age * 10.5
    else:
        dog_years = 21 + (h_age - 2) * 4

    return dog_years

# Test cases




def check(candidate):
    assert dog_age(12)==61
    assert dog_age(15)==73
    assert dog_age(24)==109

check(dog_age)