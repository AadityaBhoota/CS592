def count_vowels(test_str):
    vowels = set('aeiou')
    char_list = list(test_str)
    count = 0

    for i in range(len(char_list)):
        if i == 0 or i == len(char_list) - 1:
            if char_list[i] in vowels:
                count += 1
        else:
            if char_list[i-1] in vowels and char_list[i+1] in vowels:
                count += 1

    return count

def check(candidate):
    assert count_vowels('bestinstareels') == 7
    assert count_vowels('partofthejourneyistheend') == 12
    assert count_vowels('amazonprime') == 5

check(count_vowels)