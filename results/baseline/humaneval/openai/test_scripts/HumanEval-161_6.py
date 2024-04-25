def solve(s):
    new_str = ""
    has_letter = False
    for char in s:
        if char.isalpha():
            new_str += char.swapcase()  # Toggle case of the letter
            has_letter = True
        else:
            new_str += char

    if not has_letter:
        new_str = new_str[::-1]  # Reverse the string if no letters were found

    return new_str

# Test cases




def check(candidate):

    # Check some simple cases
    assert candidate("AsDf") == "aSdF"
    assert candidate("1234") == "4321"
    assert candidate("ab") == "AB"
    assert candidate("#a@C") == "#A@c"
    assert candidate("#AsdfW^45") == "#aSDFw^45"
    assert candidate("#6@2") == "2@6#"

    # Check some edge cases that are easy to work out by hand.
    assert candidate("#$a^D") == "#$A^d"
    assert candidate("#ccc") == "#CCC"

    # Don't remove this line:

check(solve)