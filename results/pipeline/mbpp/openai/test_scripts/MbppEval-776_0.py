def count_vowels(test_str):
    vowel_count = 0
    # Step 1: Iterate through each character in the string.
    for i in range(len(test_str)):
        char = test_str[i]
        # Step 2: Check if the current character and its neighboring characters (if they exist) are vowels.
        if i > 0 and i < len(test_str) - 1 and char.lower() in 'aeiou' and test_str[i-1].lower() in 'aeiou' and test_str[i+1].lower() in 'aeiou':
            # Step 3: If the condition is met, increment the count.
            vowel_count += 1
    return vowel_count

def check(candidate):
    assert count_vowels('bestinstareels') == 7
    assert count_vowels('partofthejourneyistheend') == 12
    assert count_vowels('amazonprime') == 5

check(count_vowels)