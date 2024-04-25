def rgb_to_hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0

    cmax = max(r, g, b)
    cmin = min(r, g, b)
    delta = cmax - cmin

    # Hue calculation
    if delta == 0:
        h = 0
    elif cmax == r:
        h = ((g - b) / delta) % 6
    elif cmax == g:
        h = (b - r) / delta + 2
    else:
        h = (r - g) / delta + 4
    h = round(h * 60, 8)

    # Saturation calculation
    s = 0 if cmax == 0 else delta / cmax
    s = round(s * 100, 8)

    # Value calculation
    v = round(cmax * 100, 8)

    return (h, s, v)

# Test cases




def check(candidate):
    assert rgb_to_hsv(255, 255, 255)==(0, 0.0, 100.0)
    assert rgb_to_hsv(0, 215, 0)==(120.0, 100.0, 84.31372549019608)
    assert rgb_to_hsv(10, 215, 110)==(149.26829268292684, 95.34883720930233, 84.31372549019608)

check(rgb_to_hsv)