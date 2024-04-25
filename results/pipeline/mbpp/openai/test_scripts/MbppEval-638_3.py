import math

def wind_chill(v, t):
    celsius_to_fahrenheit = (t * 9/5) + 32
    wind_chill_index = 13.12 + 0.6215 * celsius_to_fahrenheit - 11.37 * v**0.16 + 0.3965 * celsius_to_fahrenheit * v**0.16
    rounded_wind_chill_index = round(wind_chill_index)
    return rounded_wind_chill_index

def check(candidate):
    assert wind_chill(120,35)==40
    assert wind_chill(40,20)==19
    assert wind_chill(10,8)==6

check(wind_chill)