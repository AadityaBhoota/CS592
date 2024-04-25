def reverse_words(s):
    word_list = s.split()
    reversed_words = ' '.join(word_list[::-1])
    return reversed_words

def check(candidate):
    assert reverse_words("python program")==("program python")
    assert reverse_words("java language")==("language java")
    assert reverse_words("indian man")==("man indian")

check(reverse_words)