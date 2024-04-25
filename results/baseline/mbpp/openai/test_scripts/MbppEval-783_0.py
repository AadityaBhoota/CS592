def rgb_to_hsv(r, g, b):
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    max_val = max(r, g, b)
    min_val = min(r, g, b)
    diff = max_val - min_val

    if max_val == min_val:
        h = 0
    elif max_val == r:
        h = 60 * ((g - b) / diff % 6)
    elif max_val == g:
        h = 60 * ((b - r) / diff + 2)
    else:
        h = 60 * ((r - g) / diff + 4)

    if max_val == 0:
        s = 0
    else:
        s = diff / max_val

    v = max_val

    return h, s * 100, v * 100

# Test cases




def check(candidate):
    assert rgb_to_hsv(255, 255, 255)==(0, 0.0, 100.0)
    assert rgb_to_hsv(0, 215, 0)==(120.0, 100.0, 84.31372549019608)
    assert rgb_to_hsv(10, 215, 110)==(149.26829268292684, 95.34883720930233, 84.31372549019608)

check(rgb_to_hsv)