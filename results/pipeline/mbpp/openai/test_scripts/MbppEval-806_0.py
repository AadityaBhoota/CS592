def max_run_uppercase(test_str):
    max_count = 0
    count = 0

    for char in test_str:
        if char.isupper():
            count += 1
        else:
            if count > max_count:
                max_count = count
            count = 0

    if count > max_count:
        max_count = count

    return max_count

def check(candidate):
    assert max_run_uppercase('GeMKSForGERksISBESt') == 5
    assert max_run_uppercase('PrECIOusMOVemENTSYT') == 6
    assert max_run_uppercase('GooGLEFluTTER') == 4

check(max_run_uppercase)