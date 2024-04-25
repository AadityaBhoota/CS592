def sample_nam(sample_names):
    total_length = 0
    
    for name in sample_names:
        if name[0].islower():
            continue

        total_length += len(name)  # Implementing step 4
    
    return total_length

def check(candidate):
    assert sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])==16
    assert sample_nam(["php", "res", "Python", "abcd", "Java", "aaa"])==10
    assert sample_nam(["abcd", "Python", "abba", "aba"])==6

check(sample_nam)