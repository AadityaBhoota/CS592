def encode(message):
    encoded_message = ''
    for char in message:
        if char.isalpha():
            if char.lower() in 'aeiou':
                new_char = chr((ord(char.lower()) - 'a' + 2) % 26 + 'a')
                encoded_message += new_char.upper() if char.isupper() else new_char
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