def encode(message):
    vowels = 'aeiouAEIOU'
    encoding_dict = {'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w',
                     'A': 'C', 'E': 'G', 'I': 'K', 'O': 'Q', 'U': 'W'}
    
    encoded_message = ''
    for char in message:
        if char in vowels:
            encoded_message += encoding_dict.get(char, char)
        else:
            encoded_message += char.swapcase()
    
    return encoded_message

def check(candidate):

    # Check some simple cases
    assert candidate('TEST') == 'tgst', "This prints if this assert fails 1 (good for debugging!)"
    assert candidate('Mudasir') == 'mWDCSKR', "This prints if this assert fails 2 (good for debugging!)"
    assert candidate('YES') == 'ygs', "This prints if this assert fails 3 (good for debugging!)"
    
    # Check some edge cases that are easy to work out by hand.
    assert candidate('This is a message') == 'tHKS KS C MGSSCGG', "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate("I DoNt KnOw WhAt tO WrItE") == 'k dQnT kNqW wHcT Tq wRkTg', "This prints if this assert fails 2 (also good for debugging!)"


check(encode)