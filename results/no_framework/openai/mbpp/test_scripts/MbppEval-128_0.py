def long_words(n, text):
    words = text.split()
    result = [word for word in words if len(word) > n]
    return result

# Test cases




def check(candidate):
    assert long_words(3,"python is a programming language")==['python','programming','language']
    assert long_words(2,"writing a program")==['writing','program']
    assert long_words(5,"sorting list")==['sorting']

check(long_words)