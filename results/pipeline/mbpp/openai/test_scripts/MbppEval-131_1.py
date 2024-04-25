def reverse_vowels(str1):
    vowels = ["a", "e", "i", "o", "u"]
    char_list = list(str1)
    
    start = 0
    end = len(char_list) - 1
    
    while start < end:
        if char_list[start].lower() in vowels and char_list[end].lower() in vowels:
            char_list[start], char_list[end] = char_list[end], char_list[start]
            
        start += 1
        end -= 1
    
    return "".join(char_list)

def check(candidate):
    assert reverse_vowels("Python") == "Python"
    assert reverse_vowels("USA") == "ASU"
    assert reverse_vowels("ab") == "ab"

check(reverse_vowels)