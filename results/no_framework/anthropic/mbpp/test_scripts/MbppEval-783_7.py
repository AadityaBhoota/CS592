def rgb_to_hsv(r, g, b):
    """
    Converts an RGB color to HSV color space.

    Args:
        r (int): The red component of the color, in the range [0, 255].
        g (int): The green component of the color, in the range [0, 255].
        b (int): The blue component of the color, in the range [0, 255].

    Returns:
        tuple: A tuple of three floats in the range [0.0, 360.0] for the hue,
        [0.0, 100.0] for the saturation, and [0.0, 100.0] for the value.
    """
    # Convert RGB values to the range [0, 1]
    r, g, b = r / 255.0, g / 255.0, b / 255.0

    # Calculate the maximum and minimum of R, G, and B
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx - mn

    # Calculate the hue
    if mx == mn:
        h = 0.0
    elif mx == r:
        h = (60.0 * ((g - b) / df) + 360.0) % 360.0
    elif mx == g:
        h = (60.0 * ((b - r) / df) + 120.0) % 360.0
    elif mx == b:
        h = (60.0 * ((r - g) / df) + 240.0) % 360.0

    # Calculate the saturation
    if mx == 0:
        s = 0.0
    else:
        s = (df / mx) * 100.0

    # Calculate the value
    v = mx * 100.0

    return h, s, v

def check(candidate):
    assert rgb_to_hsv(255, 255, 255)==(0, 0.0, 100.0)
    assert rgb_to_hsv(0, 215, 0)==(120.0, 100.0, 84.31372549019608)
    assert rgb_to_hsv(10, 215, 110)==(149.26829268292684, 95.34883720930233, 84.31372549019608)

check(rgb_to_hsv)