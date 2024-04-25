def get_closest_vowel(word):
    vowels = 'aeiouAEIOU'
    last_consonant = -1

    for i, char in enumerate(word):
        if char in vowels:
            if last_consonant >= 0 and i < len(word) - 1 and word[i+1] not in vowels:
                return char
        elif char not in vowels:
            last_consonant = i

    return ""

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