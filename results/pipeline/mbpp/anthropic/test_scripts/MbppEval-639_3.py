def sample_nam(sample_names):
    uppercase_names = [name for name in sample_names if name[0].isupper()]
    return sum(len(name) for name in uppercase_names)

def check(candidate):
    assert sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])==16
    assert sample_nam(["php", "res", "Python", "abcd", "Java", "aaa"])==10
    assert sample_nam(["abcd", "Python", "abba", "aba"])==6

check(sample_nam)