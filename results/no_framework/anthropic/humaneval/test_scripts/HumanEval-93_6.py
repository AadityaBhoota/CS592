def encode(message):
    """
    Encodes the given message by swapping the case of all letters and replacing vowels with
    the letter that appears 2 places ahead of the vowel in the English alphabet.
    """
    vowels = 'aeiou'
    encoded_message = ''
    for char in message:
        if char.isalpha():
            if char.lower() in vowels:
                new_char = chr(ord(char.lower()) + 2)
                if new_char > 'z':
                    new_char = chr(ord(new_char) - 26)
                if char.isupper():
                    encoded_message += new_char.upper()
                else:
                    encoded_message += new_char
            else:
                encoded_message += char.swapcase()
        else:
            encoded_message += char
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