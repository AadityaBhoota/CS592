def get_closest_vowel(word):
    vowels = set("aeiouAEIOU")
    
    for i in range(len(word) - 1, 0, -1):  # from the last character (excluding) to the second character
        if word[i].isalpha() and not word[i].lower() in vowels:  # check for consonant
            if word[i-1].isalpha() and not word[i-1].lower() in vowels and word[i+1].isalpha() and not word[i+1].lower() in vowels:
                for v in range(i+1, len(word)):
                    if word[v].isalpha() and word[v].lower() in vowels:
                        return word[v]
    
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