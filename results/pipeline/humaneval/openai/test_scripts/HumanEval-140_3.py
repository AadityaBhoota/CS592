def fix_spaces(text):
    result = ""
    current_consecutive_spaces = 0  # count of consecutive spaces
    
    for i, char in enumerate(text):
        if char == " ":
            current_consecutive_spaces += 1

            if i + 1 < len(text) and text[i + 1] == " ":
                current_consecutive_spaces += 1
                
                if current_consecutive_spaces > 2:
                    result += "-"
                else:
                    result += "_"
            else:
                result += "_"
        else:
            current_consecutive_spaces = 0
            result += char

    return result

def check(candidate):

    # Check some simple cases
    assert candidate("Example") == "Example", "This prints if this assert fails 1 (good for debugging!)"
    assert candidate("Mudasir Hanif ") == "Mudasir_Hanif_", "This prints if this assert fails 2 (good for debugging!)"
    assert candidate("Yellow Yellow  Dirty  Fellow") == "Yellow_Yellow__Dirty__Fellow", "This prints if this assert fails 3 (good for debugging!)"
    
    # Check some edge cases that are easy to work out by hand.
    assert candidate("Exa   mple") == "Exa-mple", "This prints if this assert fails 4 (good for debugging!)"
    assert candidate("   Exa 1 2 2 mple") == "-Exa_1_2_2_mple", "This prints if this assert fails 4 (good for debugging!)"


check(fix_spaces)