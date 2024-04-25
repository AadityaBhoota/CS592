def split(word): 
    characters = []
    for char in word:
        characters.append(char)
    return characters

def check(candidate):
    assert split('python') == ['p','y','t','h','o','n']
    assert split('Name') == ['N','a','m','e']
    assert split('program') == ['p','r','o','g','r','a','m']

check(split)