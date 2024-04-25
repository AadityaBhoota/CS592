def max_run_uppercase(test_str):
    """
    Find the maximum run of uppercase characters in the given string.

    Examples:
    max_run_uppercase('GeMKSForGERksISBESt') == 5
    max_run_uppercase('PrECIOusMOVemENTSYT') == 6
    max_run_uppercase('GooGLEFluTTER') == 4
    """
    max_count = 0
    current_count = 0

    for char in test_str:
        if char.isupper():
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0

    return max_count

def check(candidate):
    assert max_run_uppercase('GeMKSForGERksISBESt') == 5
    assert max_run_uppercase('PrECIOusMOVemENTSYT') == 6
    assert max_run_uppercase('GooGLEFluTTER') == 4

check(max_run_uppercase)