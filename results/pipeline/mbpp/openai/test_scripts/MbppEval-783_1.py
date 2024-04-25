import colorsys

def rgb_to_hsv(r, g, b):
    r_norm = r / 255
    g_norm = g / 255
    b_norm = b / 255
    
    h, s, v = colorsys.rgb_to_hsv(r_norm, g_norm, b_norm)
    
    h = h * 360
    s = s * 100
    v = v * 100
    
    return h, s, v

def check(candidate):
    assert rgb_to_hsv(255, 255, 255)==(0, 0.0, 100.0)
    assert rgb_to_hsv(0, 215, 0)==(120.0, 100.0, 84.31372549019608)
    assert rgb_to_hsv(10, 215, 110)==(149.26829268292684, 95.34883720930233, 84.31372549019608)

check(rgb_to_hsv)