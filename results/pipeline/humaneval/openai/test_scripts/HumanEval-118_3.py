def is_consonant(char):
    return char.isalpha() and char.lower() not in ['a', 'e', 'i', 'o', 'u']

def get_closest_vowel(word):
    found_consonant = False
    closest_vowel = ""
    for char in reversed(word):
        if is_consonant(char):
            found_consonant = True
        elif found_consonant and char.isalpha() and not is_consonant(char):
            closest_vowel = char
            break

    return closest_vowel

def check(candidate):

    # Check some simple cases
    assert candidate("yogurt") == "u"
    assert candidate("full") == "u"
    assert candidate("easy") == ""
    assert candidate("eAsy") == ""
    assert candidate("ali") == ""
    assert candidate("bad") == "a"
    assert candidate("most") == "o"
    assert candidate("ab") == ""
    assert candidate("ba") == ""
    assert candidate("quick") == ""
    assert candidate("anime") == "i"
    assert candidate("Asia") == ""
    assert candidate("Above") == "o"

    # Check some edge cases that are easy to work out by hand.
    assert True


check(get_closest_vowel)