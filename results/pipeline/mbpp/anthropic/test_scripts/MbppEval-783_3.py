def rgb_to_hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx - mn
    if mx == 0:
        s = 0
    else:
        s = (df/mx)*100
    if df == 0:
        h = 0
    elif mx == r:
        h = (g - b)/df * 60 + 0
    elif mx == g:
        h = (b - r)/df * 60 + 120
    elif mx == b:
        h = (r - g)/df * 60 + 240
    if h < 0:
        h += 360
    return h, s, mx*100

def check(candidate):
    assert rgb_to_hsv(255, 255, 255)==(0, 0.0, 100.0)
    assert rgb_to_hsv(0, 215, 0)==(120.0, 100.0, 84.31372549019608)
    assert rgb_to_hsv(10, 215, 110)==(149.26829268292684, 95.34883720930233, 84.31372549019608)

check(rgb_to_hsv)