def fix_spaces(text):
    result = ""
    consecutive_spaces = 0
    for char in text:
        if char == " ":
            consecutive_spaces += 1
            if consecutive_spaces > 2:
                result = result.rstrip("_") + "-"
        else:
            result += "_" * consecutive_spaces
            result += char
            consecutive_spaces = 0

    result += "_" * consecutive_spaces
    
    return result

# Test cases





def check(candidate):

    # Check some simple cases
    assert candidate("Example") == "Example", "This prints if this assert fails 1 (good for debugging!)"
    assert candidate("Mudasir Hanif ") == "Mudasir_Hanif_", "This prints if this assert fails 2 (good for debugging!)"
    assert candidate("Yellow Yellow  Dirty  Fellow") == "Yellow_Yellow__Dirty__Fellow", "This prints if this assert fails 3 (good for debugging!)"
    
    # Check some edge cases that are easy to work out by hand.
    assert candidate("Exa   mple") == "Exa-mple", "This prints if this assert fails 4 (good for debugging!)"
    assert candidate("   Exa 1 2 2 mple") == "-Exa_1_2_2_mple", "This prints if this assert fails 4 (good for debugging!)"


check(fix_spaces)