def reverse_vowels(str1):
    vowels = set("aeiouAEIOU")
    vowels_found = []
    
    for char in str1:
        if char in vowels:
            vowels_found.append(char)
    
    reversed_vowels = vowels_found[::-1]

    modified_str = ""
    for char in str1:
        if char in vowels:
            modified_str += reversed_vowels.pop()
        else:
            modified_str += char
    
    return modified_str

def check(candidate):
    assert reverse_vowels("Python") == "Python"
    assert reverse_vowels("USA") == "ASU"
    assert reverse_vowels("ab") == "ab"

check(reverse_vowels)