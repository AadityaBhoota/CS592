def reverse_vowels(str1):
    vowels = 'aeiouAEIOU'
    str_list = list(str1)
    
    left_ptr, right_ptr = 0, len(str_list) - 1
    
    while left_ptr < right_ptr:
        if str_list[left_ptr] in vowels and str_list[right_ptr] in vowels:
            str_list[left_ptr], str_list[right_ptr] = str_list[right_ptr], str_list[left_ptr]
            left_ptr += 1
            right_ptr -= 1
        elif str_list[left_ptr] not in vowels:
            left_ptr += 1
        elif str_list[right_ptr] not in vowels:
            right_ptr -= 1

    return ''.join(str_list)

def check(candidate):
    assert reverse_vowels("Python") == "Python"
    assert reverse_vowels("USA") == "ASU"
    assert reverse_vowels("ab") == "ab"

check(reverse_vowels)