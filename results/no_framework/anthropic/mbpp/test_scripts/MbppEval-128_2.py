def long_words(n, string):
    """
    Find words that are longer than n characters from a given string.

    Args:
        n (int): The minimum length of the words to be returned.
        string (str): The input string containing words.

    Returns:
        list: A list of words longer than n characters.
    """
    words = string.split()
    long_words = [word for word in words if len(word) > n]
    return long_words

def check(candidate):
    assert long_words(3,"python is a programming language")==['python','programming','language']
    assert long_words(2,"writing a program")==['writing','program']
    assert long_words(5,"sorting list")==['sorting']

check(long_words)