def rgb_to_hsv(r, g, b):
    r, g, b = r / 255.0, g / 255.0, b / 255.0

    max_color = max(r, g, b)
    min_color = min(r, g, b)
    
    diff = max_color - min_color

    # Calculate Hue
    if diff == 0:
        h = 0
    elif max_color == r:
        h = 60 * (((g - b) / diff) % 6)
    elif max_color == g:
        h = 60 * (((b - r) / diff) + 2)
    elif max_color == b:
        h = 60 * (((r - g) / diff) + 4)

    # Calculate Saturation
    if max_color == 0:
        s = 0
    else:
        s = (diff / max_color) * 100

    # Calculate Value
    v = max_color * 100

    return round(h, 10), round(s, 10), round(v, 10)

# Test the function with the provided examples




def check(candidate):
    assert rgb_to_hsv(255, 255, 255)==(0, 0.0, 100.0)
    assert rgb_to_hsv(0, 215, 0)==(120.0, 100.0, 84.31372549019608)
    assert rgb_to_hsv(10, 215, 110)==(149.26829268292684, 95.34883720930233, 84.31372549019608)

check(rgb_to_hsv)