import math

def rgb_to_hsv(r, g, b):
    """
    Convert RGB color to HSV color.

    Args:
        r (int): The red value, between 0 and 255.
        g (int): The green value, between 0 and 255.
        b (int): The blue value, between 0 and 255.

    Returns:
        tuple: A tuple of (h, s, v) where:
            h is the hue as a number between 0 and 360 degrees,
            s is the saturation as a number between 0 and 100 percent,
            v is the value as a number between 0 and 100 percent.
    """
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx - mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g - b) / df) + 360) % 360
    elif mx == g:
        h = (60 * ((b - r) / df) + 120) % 360
    elif mx == b:
        h = (60 * ((r - g) / df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = (df / mx) * 100
    v = mx * 100
    return h, s, v

def check(candidate):
    assert rgb_to_hsv(255, 255, 255)==(0, 0.0, 100.0)
    assert rgb_to_hsv(0, 215, 0)==(120.0, 100.0, 84.31372549019608)
    assert rgb_to_hsv(10, 215, 110)==(149.26829268292684, 95.34883720930233, 84.31372549019608)

check(rgb_to_hsv)