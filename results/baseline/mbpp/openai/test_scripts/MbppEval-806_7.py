def max_run_uppercase(test_str):
    max_run = 0
    current_run = 0
    
    for char in test_str:
        if char.isupper():
            current_run += 1
        else:
            max_run = max(max_run, current_run)
            current_run = 0

    return max(max_run, current_run)

# Test cases




def check(candidate):
    assert max_run_uppercase('GeMKSForGERksISBESt') == 5
    assert max_run_uppercase('PrECIOusMOVemENTSYT') == 6
    assert max_run_uppercase('GooGLEFluTTER') == 4

check(max_run_uppercase)