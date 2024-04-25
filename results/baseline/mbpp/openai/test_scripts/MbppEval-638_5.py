import math

def wind_chill(v, t):
    if v < 5:
        return t
    wci = math.ceil(13.12 + 0.6215*t - 11.37*math.pow(v, 0.16) + 0.3965*t*math.pow(v, 0.16))
    return wci

# Test cases




def check(candidate):
    assert wind_chill(120,35)==40
    assert wind_chill(40,20)==19
    assert wind_chill(10,8)==6

check(wind_chill)