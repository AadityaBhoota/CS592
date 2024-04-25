def fix_spaces(text):
    fixed_text = ""
    consecutive_spaces = 0
    
    for char in text:
        if char == " ":
            consecutive_spaces += 1
            if consecutive_spaces > 2:
                fixed_text = fixed_text.rstrip("_")  # Remove multiple consecutive underscores
                fixed_text += "-"
            else:
                fixed_text += "_"
        else:
            fixed_text += char
            consecutive_spaces = 0
    
    return fixed_text

def check(candidate):

    # Check some simple cases
    assert candidate("Example") == "Example", "This prints if this assert fails 1 (good for debugging!)"
    assert candidate("Mudasir Hanif ") == "Mudasir_Hanif_", "This prints if this assert fails 2 (good for debugging!)"
    assert candidate("Yellow Yellow  Dirty  Fellow") == "Yellow_Yellow__Dirty__Fellow", "This prints if this assert fails 3 (good for debugging!)"
    
    # Check some edge cases that are easy to work out by hand.
    assert candidate("Exa   mple") == "Exa-mple", "This prints if this assert fails 4 (good for debugging!)"
    assert candidate("   Exa 1 2 2 mple") == "-Exa_1_2_2_mple", "This prints if this assert fails 4 (good for debugging!)"


check(fix_spaces)