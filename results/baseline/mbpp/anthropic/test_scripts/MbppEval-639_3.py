def sample_nam(sample_names):
    """
    Write a function to sum the length of the names of a given list of names after removing the names that start with a lowercase letter.

    Examples:
    sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']) == 16
    sample_nam(["php", "res", "Python", "abcd", "Java", "aaa"]) == 10
    sample_nam(["abcd", "Python", "abba", "aba"]) == 6
    """
    return sum(len(name) for name in sample_names if name[0].isupper())

def check(candidate):
    assert sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])==16
    assert sample_nam(["php", "res", "Python", "abcd", "Java", "aaa"])==10
    assert sample_nam(["abcd", "Python", "abba", "aba"])==6

check(sample_nam)