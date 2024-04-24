def fix_spaces(text):
    result = ''
    count = 0

    for char in text:
        if char == " ":
            count += 1
            if count > 2:
                result = result[:-2] + "-"  # Replace more than 2 consecutive spaces with a single dash
        else:
            if count > 1 and count < 3:
                result += "_"
            elif count > 2:
                result += "-"
            result += char
            count = 0

    return result

# Test cases
print(fix_spaces("Example"))  # "Example"
print(fix_spaces("Example 1"))  # "Example_1"
print(fix_spaces(" Example 2"))  # "_Example_2"
print(fix_spaces(" Example   3"))  # "_Example-3"

def check(candidate):

    # Check some simple cases
    assert candidate("Example") == "Example", "This prints if this assert fails 1 (good for debugging!)"
    assert candidate("Mudasir Hanif ") == "Mudasir_Hanif_", "This prints if this assert fails 2 (good for debugging!)"
    assert candidate("Yellow Yellow  Dirty  Fellow") == "Yellow_Yellow__Dirty__Fellow", "This prints if this assert fails 3 (good for debugging!)"
    
    # Check some edge cases that are easy to work out by hand.
    assert candidate("Exa   mple") == "Exa-mple", "This prints if this assert fails 4 (good for debugging!)"
    assert candidate("   Exa 1 2 2 mple") == "-Exa_1_2_2_mple", "This prints if this assert fails 4 (good for debugging!)"


check(fix_spaces)