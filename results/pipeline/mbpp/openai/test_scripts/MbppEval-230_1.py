def replace_blank(str1, char):
    # Step 0: Check if the inputs are valid
    if not isinstance(str1, str) or len(str1) == 0 or not isinstance(char, str) or len(char) != 1:
        return "Invalid input. Please provide a non-empty string and a single character."

    # Step 1: Replace all occurrences of blank spaces with the character
    new_str = str1.replace(' ', char)

    # Step 2: Return the modified string
    return new_str

def check(candidate):
    assert replace_blank("hello people",'@')==("hello@people")
    assert replace_blank("python program language",'$')==("python$program$language")
    assert replace_blank("blank space","-")==("blank-space")

check(replace_blank)