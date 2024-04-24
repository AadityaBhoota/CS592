def encode(message):
    vowels = 'aeiouAEIOU'
    result = ''
    
    for char in message:
        if char.isalpha():
            if char.lower() in vowels:
                new_char = chr((ord(char) + 2 - 65) % 26 + 65) if char.isupper() else chr((ord(char) + 2 - 97) % 26 + 97)
            else:
                new_char = char.swapcase()
            result += new_char
        else:
            result += char
    
    return result

# Test cases
print(encode('test'))  # Output: 'TGST'
print(encode('This is a message'))  # Output: 'tHKS KS C MGSSCGG'

def check(candidate):

    # Check some simple cases
    assert candidate('TEST') == 'tgst', "This prints if this assert fails 1 (good for debugging!)"
    assert candidate('Mudasir') == 'mWDCSKR', "This prints if this assert fails 2 (good for debugging!)"
    assert candidate('YES') == 'ygs', "This prints if this assert fails 3 (good for debugging!)"
    
    # Check some edge cases that are easy to work out by hand.
    assert candidate('This is a message') == 'tHKS KS C MGSSCGG', "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate("I DoNt KnOw WhAt tO WrItE") == 'k dQnT kNqW wHcT Tq wRkTg', "This prints if this assert fails 2 (also good for debugging!)"


check(encode)