def split(word):
    return [char for char in word]

# Test the function with the given examples



def check(candidate):
    assert split('python') == ['p','y','t','h','o','n']
    assert split('Name') == ['N','a','m','e']
    assert split('program') == ['p','r','o','g','r','a','m']

check(split)