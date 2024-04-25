def reverse_vowels(str1):
    left = 0
    right = len(str1) - 1
    
    str_list = list(str1)
    
    vowels = set("aeiouAEIOU")
    
    while left < right:
        if str_list[left] not in vowels:
            left += 1
        elif str_list[right] not in vowels:
            right -= 1
        else:
            str_list[left], str_list[right] = str_list[right], str_list[left]
            left += 1
            right -= 1
    
    return "".join(str_list)

def check(candidate):
    assert reverse_vowels("Python") == "Python"
    assert reverse_vowels("USA") == "ASU"
    assert reverse_vowels("ab") == "ab"

check(reverse_vowels)