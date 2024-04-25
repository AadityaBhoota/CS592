def count_charac(str1):
    count = 0
    for char in str1:
        count += 1
    return count

# Let's test the function with some examples




def check(candidate):
    assert count_charac("python programming")==18
    assert count_charac("language")==8
    assert count_charac("words")==5

check(count_charac)