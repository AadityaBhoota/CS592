import re

def start_withp(words):
    """
    Write a function to return two words from a list of words starting with letter 'p'.

    Examples:
    start_withp(["Python PHP", "Java JavaScript", "c c++"]) == ('Python', 'PHP')
    start_withp(["Python Programming","Java Programming"]) == ('Python','Programming')
    start_withp(["Pqrst Pqr","qrstuv"]) == ('Pqrst','Pqr')
    """
    # Use a regular expression to find words starting with 'p'
    pattern = r'\bp\w*\b'
    matches = re.findall(pattern, ' '.join(words))

    # Return the first two matches, or empty strings if there are fewer than two matches
    return tuple(matches[:2]) if matches else ('', '')

def check(candidate):
    assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
    assert start_withp(["Python Programming","Java Programming"])==('Python','Programming')
    assert start_withp(["Pqrst Pqr","qrstuv"])==('Pqrst','Pqr')

check(start_withp)