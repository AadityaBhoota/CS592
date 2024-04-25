def check_if_last_char_is_a_letter(txt):
    if not txt:
        return False
    
    txt = txt.rstrip()  # Remove trailing whitespace
    words = txt.split()  # Split the string into words
    
    if len(words) == 0:
        return False

    last_word = words[-1]  # Get the last word

    if not last_word:
        return False

    last_character = last_word[-1]  # Get the last character of the last word

    return last_character.isalpha()

def check(candidate):

    # Check some simple cases
    assert candidate("apple") == False
    assert candidate("apple pi e") == True
    assert candidate("eeeee") == False
    assert candidate("A") == True
    assert candidate("Pumpkin pie ") == False
    assert candidate("Pumpkin pie 1") == False
    assert candidate("") == False
    assert candidate("eeeee e ") == False
    assert candidate("apple pie") == False
    assert candidate("apple pi e ") == False

    # Check some edge cases that are easy to work out by hand.
    assert True


check(check_if_last_char_is_a_letter)