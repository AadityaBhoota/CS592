def reverse_vowels(str1):
    vowels = ['a', 'e', 'i', 'o', 'u']
    char_list = list(str1)
    vowel_list = [char for char in char_list if char.lower() in vowels]
    vowel_list.reverse()
    
    result = []
    vowel_index = 0
    for char in char_list:
        if char.lower() in vowels:
            result.append(vowel_list[vowel_index])
            vowel_index += 1
        else:
            result.append(char)
    
    return ''.join(result)

def check(candidate):
    assert reverse_vowels("Python") == "Python"
    assert reverse_vowels("USA") == "ASU"
    assert reverse_vowels("ab") == "ab"

check(reverse_vowels)