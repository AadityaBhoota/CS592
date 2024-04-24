def reverse_vowels(str1):
    """
    Write a python function to reverse only the vowels of a given string (where y is not a vowel).

    Examples:
    reverse_vowels("Python") == "Python"
    reverse_vowels("USA") == "ASU"
    reverse_vowels("ab") == "ab"
    """
    vowels = "aeiou"
    char_list = list(str1)
    i, j = 0, len(char_list) - 1
    
    while i < j:
        if char_list[i].lower() in vowels:
            if char_list[j].lower() in vowels:
                char_list[i], char_list[j] = char_list[j], char_list[i]
                i += 1
                j -= 1
            else:
                j -= 1
        else:
            i += 1
    
    return ''.join(char_list)

def check(candidate):
    assert reverse_vowels("Python") == "Python"
    assert reverse_vowels("USA") == "ASU"
    assert reverse_vowels("ab") == "ab"

check(reverse_vowels)