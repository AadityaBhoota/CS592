import math

def wind_chill(v, t):
    # Step 1: Convert wind speed from km/h to m/s
    v_ms = v * 1000 / 3600  # Convert km/h to m/s
    
    # Step 2: Compute the wind chill index
    wind_chill_index = round(13.12 + 0.6215 * t - 11.37 * (v_ms**0.16) + 0.3965 * t * (v_ms**0.16))
    
    # Step 3: Return the rounded wind chill index
    return wind_chill_index

def check(candidate):
    assert wind_chill(120,35)==40
    assert wind_chill(40,20)==19
    assert wind_chill(10,8)==6

check(wind_chill)