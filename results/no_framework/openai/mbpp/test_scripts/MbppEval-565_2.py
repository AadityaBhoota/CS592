def split(word):
    # Using list comprehension to split the word into characters
    return [char for char in word]
    
# Test cases




def check(candidate):
    assert split('python') == ['p','y','t','h','o','n']
    assert split('Name') == ['N','a','m','e']
    assert split('program') == ['p','r','o','g','r','a','m']

check(split)