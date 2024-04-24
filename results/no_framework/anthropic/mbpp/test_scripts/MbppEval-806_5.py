def max_run_uppercase(test_str):
    """
    Write a function to find the maximum run of uppercase characters in the given string.

    Examples:
    max_run_uppercase('GeMKSForGERksISBESt') == 5
    max_run_uppercase('PrECIOusMOVemENTSYT') == 6
    max_run_uppercase('GooGLEFluTTER') == 4
    """
    max_run = 0
    current_run = 0

    for char in test_str:
        if char.isupper():
            current_run += 1
            max_run = max(max_run, current_run)
        else:
            current_run = 0

    return max_run

def check(candidate):
    assert max_run_uppercase('GeMKSForGERksISBESt') == 5
    assert max_run_uppercase('PrECIOusMOVemENTSYT') == 6
    assert max_run_uppercase('GooGLEFluTTER') == 4

check(max_run_uppercase)