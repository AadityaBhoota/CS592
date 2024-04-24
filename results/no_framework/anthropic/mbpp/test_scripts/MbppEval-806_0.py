def max_run_uppercase(test_str):
    """
    Find the maximum run of uppercase characters in the given string.

    Args:
        test_str (str): The input string.

    Returns:
        int: The length of the maximum run of uppercase characters.
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