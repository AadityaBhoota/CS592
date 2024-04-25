def reverse_words(s):
    words = s.split()
    reversed_words = words[::-1]
    reversed_str = ' '.join(reversed_words)
    return reversed_str

def check(candidate):
    assert reverse_words("python program")==("program python")
    assert reverse_words("java language")==("language java")
    assert reverse_words("indian man")==("man indian")

check(reverse_words)