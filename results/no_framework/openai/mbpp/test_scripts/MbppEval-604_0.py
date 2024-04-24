def reverse_words(s):
    words = s.split()
    reversed_words = " ".join(words[::-1])
    return reversed_words

# Test cases




def check(candidate):
    assert reverse_words("python program")==("program python")
    assert reverse_words("java language")==("language java")
    assert reverse_words("indian man")==("man indian")

check(reverse_words)