def dog_age(h_age):
    if h_age <= 0:
        return "Invalid age. Please provide a positive number."
    
    if h_age <= 2:
        d_age = h_age * 10.5
    else:
        d_age = 2 * 10.5 + (h_age - 2) * 4
    
    return int(d_age)

def check(candidate):
    assert dog_age(12)==61
    assert dog_age(15)==73
    assert dog_age(24)==109

check(dog_age)