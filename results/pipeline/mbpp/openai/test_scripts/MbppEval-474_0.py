def replace_char(str1, ch, newch):
    modified_str = ''

    # Loop through each character in the input string
    for char in str1:
        # Check if the character matches the specific character 'ch' that needs to be replaced
        if char == ch:
            # If the character matches, replace it with the new character 'newch'
            modified_str += newch
        else:
            modified_str += char
    
    return modified_str

# Test the function


def check(candidate):
    assert replace_char("polygon",'y','l')==("pollgon")
    assert replace_char("character",'c','a')==("aharaater")
    assert replace_char("python",'l','a')==("python")

check(replace_char)