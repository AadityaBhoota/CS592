def reverse_vowels(str1):
    vowels = "aeiouAEIOU"
    str_list = list(str1)
    i, j = 0, len(str_list) - 1
    
    while i < j:
        if str_list[i] in vowels and str_list[j] in vowels:
            str_list[i], str_list[j] = str_list[j], str_list[i]
            i += 1
            j -= 1
        elif str_list[i] in vowels:
            j -= 1
        elif str_list[j] in vowels:
            i += 1
        else:
            i += 1
            j -= 1
    
    return "".join(str_list)

# Test cases




def check(candidate):
    assert reverse_vowels("Python") == "Python"
    assert reverse_vowels("USA") == "ASU"
    assert reverse_vowels("ab") == "ab"

check(reverse_vowels)