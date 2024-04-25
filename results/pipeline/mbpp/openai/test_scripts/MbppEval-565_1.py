def split(word): 
    result = []  # Initialize an empty list to store characters
    
    for char in word: 
        result.append(char)  # Append each character to the list
        
    return result

def check(candidate):
    assert split('python') == ['p','y','t','h','o','n']
    assert split('Name') == ['N','a','m','e']
    assert split('program') == ['p','r','o','g','r','a','m']

check(split)