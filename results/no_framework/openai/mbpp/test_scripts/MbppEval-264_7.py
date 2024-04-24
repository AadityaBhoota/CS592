def dog_age(h_age):
    if h_age <= 0:
        return "Invalid age input"
    elif h_age == 1:
        return 15
    elif h_age == 2:
        return 24
    else:
        dog_years = 24 + (h_age - 2) * 5
        return dog_years

def check(candidate):
    assert dog_age(12)==61
    assert dog_age(15)==73
    assert dog_age(24)==109

check(dog_age)