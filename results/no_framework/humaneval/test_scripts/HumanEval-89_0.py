def encrypt(s):
    result = ""
    for char in s:
        if char.isalpha():
            shift = (ord(char.lower()) - ord('a') + 2) * 2
            shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result += shifted_char
        else:
            result += char
    return result

# Test cases
print(encrypt('hi'))        # Output: 'lm'
print(encrypt('asdfghjkl'))  # Output: 'ewhjklnop'
print(encrypt('gf'))        # Output: 'kj'
print(encrypt('et'))        # Output: 'ix'

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