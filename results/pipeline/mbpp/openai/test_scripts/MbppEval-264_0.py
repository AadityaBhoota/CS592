def dog_age(h_age):
    dog_age = 0
    
    if h_age <= 0:
        return dog_age
    
    if h_age == 1:
        dog_age += 10.5
    elif h_age == 2:
        dog_age += 10.5 + 4
    else:
        dog_age += 10.5 + 4 + (h_age - 2) * 4
    
    return dog_age

def check(candidate):
    assert dog_age(12)==61
    assert dog_age(15)==73
    assert dog_age(24)==109

check(dog_age)