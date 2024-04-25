def count_vowels(test_str):
    vowel_count = 0
    vowels = 'aeiouAEIOU'
    
    for i in range(1, len(test_str) - 1):
        char = test_str[i]
        before = test_str[i - 1]
        after = test_str[i + 1]
        
        if any(c in vowels for c in [char, before, after]):
            vowel_count += 1

    return vowel_count

def check(candidate):
    assert count_vowels('bestinstareels') == 7
    assert count_vowels('partofthejourneyistheend') == 12
    assert count_vowels('amazonprime') == 5

check(count_vowels)