def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """
    
    # Define the alphabet mapping
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    # Iterate through each character in the input string
    encrypted_chars = []
    for char in s:
        # Check if the character is a letter
        if char.isalpha():
            # Find the position of the character in the alphabet
            if char.islower():
                pos = alphabet_lower.index(char)
            else:
                pos = alphabet_upper.index(char)
            
            # Shift the position by 4 places
            new_pos = (pos + 4) % len(alphabet_lower)
            
            # Replace the character with the new shifted character
            if char.islower():
                encrypted_chars.append(alphabet_lower[new_pos])
            else:
                encrypted_chars.append(alphabet_upper[new_pos])
        else:
            # Keep non-alphabetic characters as-is
            encrypted_chars.append(char)
    
    # Return the encrypted string
    return ''.join(encrypted_chars)

def check(candidate):

    # Check some simple cases
    assert candidate('hi') == 'lm', "This prints if this assert fails 1 (good for debugging!)"
    assert candidate('asdfghjkl') == 'ewhjklnop', "This prints if this assert fails 1 (good for debugging!)"
    assert candidate('gf') == 'kj', "This prints if this assert fails 1 (good for debugging!)"
    assert candidate('et') == 'ix', "This prints if this assert fails 1 (good for debugging!)"

    assert candidate('faewfawefaewg')=='jeiajeaijeiak', "This prints if this assert fails 1 (good for debugging!)"
    assert candidate('hellomyfriend')=='lippsqcjvmirh', "This prints if this assert fails 2 (good for debugging!)"
    assert candidate('dxzdlmnilfuhmilufhlihufnmlimnufhlimnufhfucufh')=='hbdhpqrmpjylqmpyjlpmlyjrqpmqryjlpmqryjljygyjl', "This prints if this assert fails 3 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert candidate('a')=='e', "This prints if this assert fails 2 (also good for debugging!)"


check(encrypt)