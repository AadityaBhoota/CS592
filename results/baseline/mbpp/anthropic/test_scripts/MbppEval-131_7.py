def reverse_vowels(str1):
    # Create a list of vowels
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    # Convert the input string to a list of characters
    char_list = list(str1)
    
    # Initialize two pointers, one at the beginning and one at the end of the list
    left = 0
    right = len(char_list) - 1
    
    # Iterate until the two pointers meet
    while left < right:
        # If the character at the left pointer is a vowel and the character at the right pointer is also a vowel, swap them
        if char_list[left].lower() in vowels and char_list[right].lower() in vowels:
            char_list[left], char_list[right] = char_list[right], char_list[left]
            left += 1
            right -= 1
        # If the character at the left pointer is not a vowel, move the left pointer to the right
        elif char_list[left].lower() not in vowels:
            left += 1
        # If the character at the right pointer is not a vowel, move the right pointer to the left
        elif char_list[right].lower() not in vowels:
            right -= 1
    
    # Convert the modified list of characters back to a string
    return ''.join(char_list)

def check(candidate):
    assert reverse_vowels("Python") == "Python"
    assert reverse_vowels("USA") == "ASU"
    assert reverse_vowels("ab") == "ab"

check(reverse_vowels)