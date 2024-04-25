import math

def dog_age(h_age):
    ''' 
    Calculate a dog's age in dog's years.

    Examples:
    dog_age(12) == 61
    dog_age(15) == 73
    dog_age(24) == 109
    '''
    human_years = h_age * 7
    
    dog_years = 16 * math.log(human_years) + 31
    
    return dog_years

def check(candidate):
    assert dog_age(12)==61
    assert dog_age(15)==73
    assert dog_age(24)==109

check(dog_age)