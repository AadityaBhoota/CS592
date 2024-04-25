import re

def long_words(n, input_str):
    words_list = re.findall(r'\b\w+\b', input_str)
    long_words_list = []

    for word in words_list:
        if len(word) > n:
            long_words_list.append(word)

    return long_words_list

def check(candidate):
    assert long_words(3,"python is a programming language")==['python','programming','language']
    assert long_words(2,"writing a program")==['writing','program']
    assert long_words(5,"sorting list")==['sorting']

check(long_words)