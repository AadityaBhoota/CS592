def wind_chill(v, t):
    if v < 5 or t > 10:
        return round(t)
    else:
        wind_chill_index = 13.12 + 0.6215*t - 11.37*(v**0.16) + 0.3965*t*(v**0.16)
        return round(wind_chill_index)

# Test cases




def check(candidate):
    assert wind_chill(120,35)==40
    assert wind_chill(40,20)==19
    assert wind_chill(10,8)==6

check(wind_chill)