def count_charac(str1):
    return len(str1)

# Test the function with the examples provided



def check(candidate):
    assert count_charac("python programming")==18
    assert count_charac("language")==8
    assert count_charac("words")==5

check(count_charac)