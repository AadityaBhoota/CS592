import math

def wind_chill(v, t):
    # Constants for the wind chill formula
    a = 13.12
    b = 0.6215
    c = 11.37
    d = 0.3965

    # Calculate the wind chill index using the formula
    wind_chill_index = a + b * t - c * math.pow(v, 0.16) + d * t * math.pow(v, 0.16)

    # Round the wind chill index to the nearest integer
    wind_chill_index_rounded = int(round(wind_chill_index))

    return wind_chill_index_rounded

# Test the function with the provided examples




def check(candidate):
    assert wind_chill(120,35)==40
    assert wind_chill(40,20)==19
    assert wind_chill(10,8)==6

check(wind_chill)