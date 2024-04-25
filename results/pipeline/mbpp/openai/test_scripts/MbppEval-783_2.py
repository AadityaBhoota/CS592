def rgb_to_hsv(r, g, b):
    r /= 255.0
    g /= 255.0
    b /= 255.0
    
    minimum = min(r, g, b)
    maximum = max(r, g, b)
    delta = maximum - minimum
    
    if delta == 0:
        h = 0
    elif maximum == r:
        h = 60 * (((g - b) / delta) % 6)
    elif maximum == g:
        h = 60 * (((b - r) / delta) + 2)
    else:  # maximum == b
        h = 60 * (((r - g) / delta) + 4)
    
    if maximum == 0:
        s = 0
    else:
        s = (delta / maximum) * 100
    
    v = maximum * 100
    
    return h, s, v

def check(candidate):
    assert rgb_to_hsv(255, 255, 255)==(0, 0.0, 100.0)
    assert rgb_to_hsv(0, 215, 0)==(120.0, 100.0, 84.31372549019608)
    assert rgb_to_hsv(10, 215, 110)==(149.26829268292684, 95.34883720930233, 84.31372549019608)

check(rgb_to_hsv)