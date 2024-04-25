def dog_age(h_age):
    dog_age_first_two_years = 1 + 9
    remaining_age = h_age - 2
    remaining_age_in_dog_years = remaining_age * 4
    age_in_dog_years = dog_age_first_two_years + remaining_age_in_dog_years
    return age_in_dog_years

def check(candidate):
    assert dog_age(12)==61
    assert dog_age(15)==73
    assert dog_age(24)==109

check(dog_age)