import math

def wind_chill(v, t):
    """
    Calculate the wind chill index rounded to the next integer given the wind velocity in km/h and a temperature in Celsius.

    Parameters:
    v (float): Wind velocity in km/h
    t (float): Temperature in Celsius

    Returns:
    int: Wind chill index rounded to the next integer
    """
    if v < 4.8 or t > 10:
        return round(t)
    else:
        wind_chill_index = 13.12 + 0.6215 * t - 11.37 * v ** 0.16 + 0.3965 * t * v ** 0.16
        return math.ceil(wind_chill_index)

def check(candidate):
    assert wind_chill(120,35)==40
    assert wind_chill(40,20)==19
    assert wind_chill(10,8)==6

check(wind_chill)