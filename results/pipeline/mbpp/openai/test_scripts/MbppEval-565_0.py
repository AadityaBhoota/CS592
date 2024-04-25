def split(word):
    characters = []  # Initialize an empty list to store the individual characters.
    
    for char in word:  # Iterate through each character in the input string.
        characters.append(char)  # Append each character to the list.

    return characters  # Return the list containing the individual characters.

def check(candidate):
    assert split('python') == ['p','y','t','h','o','n']
    assert split('Name') == ['N','a','m','e']
    assert split('program') == ['p','r','o','g','r','a','m']

check(split)