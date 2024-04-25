def remove_lowercase_names(names):
    return [name for name in names if name[0].isupper()]

def calculate_total_length(names):
    return sum(len(name) for name in names)

def sample_nam(sample_names):
    filtered_names = remove_lowercase_names(sample_names)
    total_length = calculate_total_length(filtered_names)
    return total_length

def check(candidate):
    assert sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])==16
    assert sample_nam(["php", "res", "Python", "abcd", "Java", "aaa"])==10
    assert sample_nam(["abcd", "Python", "abba", "aba"])==6

check(sample_nam)