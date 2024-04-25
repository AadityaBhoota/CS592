def reverse_words(s):
    """
    Write a function to reverse words separated by spaces in a given string.

    Examples:
    reverse_words("python program") == "program python"
    reverse_words("java language") == "language java"
    reverse_words("indian man") == "man indian"
    """
    # Split the input string into a list of words
    words = s.split()
    
    # Reverse the order of the words
    reversed_words = words[::-1]
    
    # Join the reversed words back into a string
    reversed_sentence = ' '.join(reversed_words)
    
    return reversed_sentence

def check(candidate):
    assert reverse_words("python program")==("program python")
    assert reverse_words("java language")==("language java")
    assert reverse_words("indian man")==("man indian")

check(reverse_words)