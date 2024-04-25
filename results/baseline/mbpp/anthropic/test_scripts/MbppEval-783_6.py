def rgb_to_hsv(r, g, b):
    """
    Convert RGB color to HSV color.
    
    Args:
        r (int): Red value in the range [0, 255].
        g (int): Green value in the range [0, 255].
        b (int): Blue value in the range [0, 255].
    
    Returns:
        tuple: HSV color as a tuple (hue, saturation, value) where:
            - hue is in the range [0.0, 360.0),
            - saturation is in the range [0.0, 100.0],
            - value is in the range [0.0, 100.0].
    """
    # Normalize RGB values to the range [0, 1]
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    
    # Compute the maximum and minimum of R, G, and B
    mx = max(r, g, b)
    mn = min(r, g, b)
    
    # Compute the hue
    if mx == mn:
        hue = 0.0
    elif mx == r:
        hue = 60.0 * ((g - b) / (mx - mn)) + 360.0
    elif mx == g:
        hue = 60.0 * ((b - r) / (mx - mn)) + 120.0
    elif mx == b:
        hue = 60.0 * ((r - g) / (mx - mn)) + 240.0
    
    # Compute the saturation
    if mx == 0:
        sat = 0.0
    else:
        sat = (1 - mn / mx) * 100.0
    
    # Compute the value
    val = mx * 100.0
    
    return hue, sat, val

def check(candidate):
    assert rgb_to_hsv(255, 255, 255)==(0, 0.0, 100.0)
    assert rgb_to_hsv(0, 215, 0)==(120.0, 100.0, 84.31372549019608)
    assert rgb_to_hsv(10, 215, 110)==(149.26829268292684, 95.34883720930233, 84.31372549019608)

check(rgb_to_hsv)