def split(word):
    """
    Write a python function to split a string into characters.

    Examples:
    split('python') == ['p','y','t','h','o','n']
    split('Name') == ['N','a','m','e']
    split('program') == ['p','r','o','g','r','a','m']
    """
    return list(word)

def check(candidate):
    assert split('python') == ['p','y','t','h','o','n']
    assert split('Name') == ['N','a','m','e']
    assert split('program') == ['p','r','o','g','r','a','m']

check(split)