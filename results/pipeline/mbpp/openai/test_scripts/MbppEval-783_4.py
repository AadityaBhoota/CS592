def rgb_to_hsv(r, g, b):
    # Step 0: Convert RGB values to the range 0 to 1
    r /= 255.0
    g /= 255.0
    b /= 255.0

    # Step 1: Find the maximum and minimum values among the normalized RGB values
    max_value = max(r, g, b)
    min_value = min(r, g, b)

    # Step 2: Calculate the value (V) as the maximum among the normalized RGB values
    V = max_value

    # Step 3: Calculate the saturation (S)
    S = 0 if V == 0 else (V - min_value) / V

    # Step 4: Calculate the hue (H) depending on which color component is the maximum
    if V == min_value:
        H = 0
    elif V == r:
        H = 60 * ((g - b) / (V - min_value)) % 360
    elif V == g:
        H = 60 * (2 + (b - r) / (V - min_value)) % 360
    else:
        H = 60 * (4 + (r - g) / (V - min_value)) % 360

    # Step 6: Adjust hue if it is negative, add 360 to make it fall within the range of 0 to 360
    if H < 0:
        H += 360

    return H, S, V

def check(candidate):
    assert rgb_to_hsv(255, 255, 255)==(0, 0.0, 100.0)
    assert rgb_to_hsv(0, 215, 0)==(120.0, 100.0, 84.31372549019608)
    assert rgb_to_hsv(10, 215, 110)==(149.26829268292684, 95.34883720930233, 84.31372549019608)

check(rgb_to_hsv)