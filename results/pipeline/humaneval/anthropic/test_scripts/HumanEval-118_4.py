def get_closest_vowel(word):
    vowels = 'aeiouAEIOU'
    last_consonant = None
    
    for i in range(len(word)-1, -1, -1):
        if word[i] not in vowels:
            last_consonant = i
        elif last_consonant is not None and i < last_consonant:
            return word[i]
    
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