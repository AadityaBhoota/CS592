def rgb_to_hsv(r, g, b):
    if not all(0 <= x <= 255 for x in (r, g, b)):
        raise ValueError("RGB values must be in range 0-255")
    
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    
    max_val = max(r, g, b)
    min_val = min(r, g, b)
    delta = max_val - min_val
    
    # Calculate hue
    if delta == 0:
        hue = 0
    elif max_val == r:
        hue = 60 * (((g - b) / delta) % 6)
    elif max_val == g:
        hue = 60 * (((b - r) / delta) + 2)
    else:
        hue = 60 * (((r - g) / delta) + 4)
    
    # Calculate saturation
    saturation = 0 if max_val == 0 else delta / max_val
    
    # Calculate value
    value = max_val
    
    return round(hue, 8), round(saturation * 100, 8), round(value * 100, 8)

def check(candidate):
    assert rgb_to_hsv(255, 255, 255)==(0, 0.0, 100.0)
    assert rgb_to_hsv(0, 215, 0)==(120.0, 100.0, 84.31372549019608)
    assert rgb_to_hsv(10, 215, 110)==(149.26829268292684, 95.34883720930233, 84.31372549019608)

check(rgb_to_hsv)