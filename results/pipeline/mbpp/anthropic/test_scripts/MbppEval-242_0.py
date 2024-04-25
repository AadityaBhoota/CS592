def count_charac(str1):
    char_count = 0
    for char in str1:
        char_count += 1
    return char_count

def check(candidate):
    assert count_charac("python programming")==18
    assert count_charac("language")==8
    assert count_charac("words")==5

check(count_charac)