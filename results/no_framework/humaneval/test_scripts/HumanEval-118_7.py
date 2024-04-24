def get_closest_vowel(word):
    vowels = "aeiouAEIOU"
    word = word.strip()
    consonants_found = 0
    
    for i in range(len(word)-1, 0, -1):
        if word[i] not in vowels:
            consonants_found += 1
        elif consonants_found >= 2:
            return word[i]
    
    return ""

# Test cases
print(get_closest_vowel("yogurt"))  # Output: "u"
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