def word_len(s):
    """
    Write a Python function to check whether the length of the word is odd or not.

    Examples:
    word_len("Hadoop") == False
    word_len("great") == True
    word_len("structure") == True
    """
    return len(s) % 2 != 0

def check(candidate):
    assert word_len("Hadoop") == False
    assert word_len("great") == True
    assert word_len("structure") == True

check(word_len)