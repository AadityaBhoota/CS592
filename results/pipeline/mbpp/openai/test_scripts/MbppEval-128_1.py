def long_words(n, input_string):
    words = input_string.split()
    return [word for word in words if len(word) > n]

def check(candidate):
    assert long_words(3,"python is a programming language")==['python','programming','language']
    assert long_words(2,"writing a program")==['writing','program']
    assert long_words(5,"sorting list")==['sorting']

check(long_words)