def encode(message):
    vowels = 'aeiouAEIOU'
    result = ''
    
    for char in message:
        if char.isalpha():
            # Swap case
            char = char.swapcase()
            
            # Replace vowels with letters that appear 2 places ahead
            if char in vowels:
                index = (ord(char) - ord('a') + 2) % 26
                if char.isupper():
                    char = chr(ord('A') + index)
                else:
                    char = chr(ord('a') + index)
        
        result += char
    
    return result

# Test cases



def check(candidate):

    # Check some simple cases
    assert candidate('TEST') == 'tgst', "This prints if this assert fails 1 (good for debugging!)"
    assert candidate('Mudasir') == 'mWDCSKR', "This prints if this assert fails 2 (good for debugging!)"
    assert candidate('YES') == 'ygs', "This prints if this assert fails 3 (good for debugging!)"
    
    # Check some edge cases that are easy to work out by hand.
    assert candidate('This is a message') == 'tHKS KS C MGSSCGG', "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate("I DoNt KnOw WhAt tO WrItE") == 'k dQnT kNqW wHcT Tq wRkTg', "This prints if this assert fails 2 (also good for debugging!)"


check(encode)