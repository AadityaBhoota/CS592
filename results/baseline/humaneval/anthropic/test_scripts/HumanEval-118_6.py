def get_closest_vowel(word):
    # Define the list of vowels
    vowels = 'aAeEiIoOuU'
    
    # Iterate through the word from the right side
    for i in range(len(word)-2, -1, -1):
        # Check if the current character is a consonant
        if word[i] not in vowels:
            # Check if the next character is a vowel
            if word[i+1] in vowels:
                # Check if the following character is a consonant
                if i+2 < len(word) and word[i+2] not in vowels:
                    # Return the vowel
                    return word[i+1]
    
    # If no vowel found, return an empty string
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