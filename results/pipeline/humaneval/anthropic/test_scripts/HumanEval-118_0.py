def get_closest_vowel(word):
    closest_vowel = ""
    in_between_consonants = False
    
    for char in word:
        if char.isalpha() and char.lower() not in "aeiou":
            in_between_consonants = True
        elif char.lower() in "aeiou":
            if in_between_consonants:
                closest_vowel = char
                in_between_consonants = False
            else:
                in_between_consonants = False
    
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