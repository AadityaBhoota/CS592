def rgb_to_hsv(r, g, b):
    """
    Convert RGB color to HSV color.

    Args:
        r (int): The red value in the range [0, 255].
        g (int): The green value in the range [0, 255].
        b (int): The blue value in the range [0, 255].

    Returns:
        tuple: The HSV values as a tuple (h, s, v), where:
            h is the hue in the range [0, 360),
            s is the saturation in the range [0, 100],
            v is the value in the range [0, 100].
    """
    # Normalize the RGB values to the range [0, 1]
    r, g, b = r/255, g/255, b/255

    # Calculate the maximum and minimum of the RGB values
    mx = max(r, g, b)
    mn = min(r, g, b)

    # Calculate the hue (H)
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/(mx-mn)) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/(mx-mn)) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/(mx-mn)) + 240) % 360

    # Calculate the saturation (S)
    if mx == 0:
        s = 0
    else:
        s = (1 - mn/mx) * 100

    # Calculate the value (V)
    v = mx * 100

    return h, s, v

def check(candidate):
    assert rgb_to_hsv(255, 255, 255)==(0, 0.0, 100.0)
    assert rgb_to_hsv(0, 215, 0)==(120.0, 100.0, 84.31372549019608)
    assert rgb_to_hsv(10, 215, 110)==(149.26829268292684, 95.34883720930233, 84.31372549019608)

check(rgb_to_hsv)