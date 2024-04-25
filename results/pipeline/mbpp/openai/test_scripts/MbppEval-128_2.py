def long_words(n, str):
    words = str.split()
    long_words_list = [word for word in words if len(word) > n]
    return long_words_list

def check(candidate):
    assert long_words(3,"python is a programming language")==['python','programming','language']
    assert long_words(2,"writing a program")==['writing','program']
    assert long_words(5,"sorting list")==['sorting']

check(long_words)