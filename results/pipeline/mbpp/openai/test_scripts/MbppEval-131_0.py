def reverse_vowels(str1):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    
    vowel_list = [char for char in str1 if char in vowels]
    
    reversed_vowels = vowel_list[::-1]

    reversed_str = ''
    index = 0
    for char in str1:
        if char in vowels:
            reversed_str += reversed_vowels[index]
            index += 1
        else:
            reversed_str += char
    
    return reversed_str

def check(candidate):
    assert reverse_vowels("Python") == "Python"
    assert reverse_vowels("USA") == "ASU"
    assert reverse_vowels("ab") == "ab"

check(reverse_vowels)