def get_closest_vowel(word):
    word = word.lower()
    vowels = set('aeiou')

    for i in range(len(word) - 3, 0, -1):
        if word[i] in vowels and word[i - 1] not in vowels and word[i + 1] not in vowels:
            return word[i].upper()

    return ""

# Test cases
print(get_closest_vowel("yogurt"))  # Output: "U"
print(get_closest_vowel("FULL"))    # Output: "U"
print(get_closest_vowel("quick"))   # Output: ""
print(get_closest_vowel("ab"))      # Output: ""

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