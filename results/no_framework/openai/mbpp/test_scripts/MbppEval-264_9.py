def dog_age(h_age):
    if h_age <= 0:
        return "Invalid age"
    elif h_age <= 2:
        dog_years = 10.5 * h_age
    else:
        dog_years = 21 + 4 * (h_age - 2)
    return dog_years

# Test cases




def check(candidate):
    assert dog_age(12)==61
    assert dog_age(15)==73
    assert dog_age(24)==109

check(dog_age)