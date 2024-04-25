def count_charac(str1):
    total_chars = 0
    for char in str1:
        total_chars += 1
    return total_chars

def check(candidate):
    assert count_charac("python programming")==18
    assert count_charac("language")==8
    assert count_charac("words")==5

check(count_charac)