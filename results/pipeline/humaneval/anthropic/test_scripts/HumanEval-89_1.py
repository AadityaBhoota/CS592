def encrypt(s):
    result = ""
    for char in s:
        if char.isalpha():
            # Shift the character by 4 places
            new_char = chr(ord(char) + 4)
            # Wrap around if the new character goes beyond 'z'
            if char.islower() and new_char > 'z':
                new_char = chr(ord(new_char) - 26)
            elif char.isupper() and new_char > 'Z':
                new_char = chr(ord(new_char) - 26)
            result += new_char
        else:
            result += char
    return result

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