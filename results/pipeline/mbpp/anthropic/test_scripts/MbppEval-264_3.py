def dog_age(h_age):
    if h_age <= 2:
        return h_age * 10.5
    else:
        return (2 * 10.5) + ((h_age - 2) * 4)

def check(candidate):
    assert dog_age(12)==61
    assert dog_age(15)==73
    assert dog_age(24)==109

check(dog_age)