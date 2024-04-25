def encode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode('test')
    'tGST'
    >>> encode('This is a message')
    'tHkS kS c mGSSCgG'
    """
    encoded_message = ""
    for char in message:
        if char.isalpha():
            if char.lower() in "aeiou":
                # Replace vowels with the letter 2 places ahead in the alphabet, and swap case
                encoded_message += chr(ord(char.lower()) + 2).swapcase()
            else:
                # Swap case for consonants
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