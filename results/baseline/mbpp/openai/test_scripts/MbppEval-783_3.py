def rgb_to_hsv(r, g, b):
    max_color = max(r, g, b)
    min_color = min(r, g, b)

    # Calculate hue
    if max_color == min_color:
        h = 0
    elif max_color == r:
        h = 60 * ((g - b) / (max_color - min_color) % 6)
    elif max_color == g:
        h = 60 * ((b - r) / (max_color - min_color) + 2)
    elif max_color == b:
        h = 60 * ((r - g) / (max_color - min_color) + 4)

    # Calculate saturation
    if max_color == 0:
        s = 0
    else:
        s = ((max_color - min_color) / max_color) * 100

    # Calculate value
    v = (max_color / 255) * 100

    return h, s, v

# Test cases




def check(candidate):
    assert rgb_to_hsv(255, 255, 255)==(0, 0.0, 100.0)
    assert rgb_to_hsv(0, 215, 0)==(120.0, 100.0, 84.31372549019608)
    assert rgb_to_hsv(10, 215, 110)==(149.26829268292684, 95.34883720930233, 84.31372549019608)

check(rgb_to_hsv)