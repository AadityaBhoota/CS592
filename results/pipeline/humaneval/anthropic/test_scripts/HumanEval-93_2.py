def encode(message):
    vowels = 'aeiou'
    vowel_map = {v: chr(ord(v) + 2) for v in vowels}
    encoded_message = ''
    for char in message:
        if char.isalpha():
            if char.lower() in vowels:
                encoded_message += vowel_map.get(char.lower(), '?')
            else:
                encoded_message += char.swapcase()
        else:
            encoded_message += ' '
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