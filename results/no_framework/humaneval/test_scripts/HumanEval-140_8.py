def fix_spaces(text):
    new_text = ""
    count = 0
    for char in text:
        if char == ' ':
            count += 1
            if count > 2:
                new_text = new_text.rstrip('_')
                new_text += '-'
            else:
                new_text += '_'
        else:
            count = 0
            new_text += char
    return new_text

# Test cases
print(fix_spaces("Example"))  # Output: "Example"
print(fix_spaces("Example 1"))  # Output: "Example_1"
print(fix_spaces(" Example 2"))  # Output: "_Example_2"
print(fix_spaces(" Example   3"))  # Output: "_Example-3"

def check(candidate):

    # Check some simple cases
    assert candidate("Example") == "Example", "This prints if this assert fails 1 (good for debugging!)"
    assert candidate("Mudasir Hanif ") == "Mudasir_Hanif_", "This prints if this assert fails 2 (good for debugging!)"
    assert candidate("Yellow Yellow  Dirty  Fellow") == "Yellow_Yellow__Dirty__Fellow", "This prints if this assert fails 3 (good for debugging!)"
    
    # Check some edge cases that are easy to work out by hand.
    assert candidate("Exa   mple") == "Exa-mple", "This prints if this assert fails 4 (good for debugging!)"
    assert candidate("   Exa 1 2 2 mple") == "-Exa_1_2_2_mple", "This prints if this assert fails 4 (good for debugging!)"


check(fix_spaces)