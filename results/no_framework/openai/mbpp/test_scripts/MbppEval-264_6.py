def dog_age(h_age):
    if h_age <= 2:
        dog_age = h_age * 10.5
    else:
        dog_age = 21 + (h_age - 2) * 4
    return dog_age

# Test the function with examples




def check(candidate):
    assert dog_age(12)==61
    assert dog_age(15)==73
    assert dog_age(24)==109

check(dog_age)