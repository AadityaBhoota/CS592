def max_run_uppercase(test_str):
    max_count = 0
    current_count = 0

    for char in test_str:
        if char.isupper():
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0

    return max_count

# Test cases




def check(candidate):
    assert max_run_uppercase('GeMKSForGERksISBESt') == 5
    assert max_run_uppercase('PrECIOusMOVemENTSYT') == 6
    assert max_run_uppercase('GooGLEFluTTER') == 4

check(max_run_uppercase)