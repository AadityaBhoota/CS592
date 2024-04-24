import math

def rgb_to_hsv(r, g, b):
    """
    Converts an RGB color to HSV color.

    Args:
        r (int): The red component of the color, in the range [0, 255].
        g (int): The green component of the color, in the range [0, 255].
        b (int): The blue component of the color, in the range [0, 255].

    Returns:
        Tuple[float, float, float]: The HSV representation of the color, where:
            - h (float): The hue component, in the range [0.0, 360.0).
            - s (float): The saturation component, in the range [0.0, 100.0].
            - v (float): The value component, in the range [0.0, 100.0].
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