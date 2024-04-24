def solve(s):
    new_s = ''
    letters = False
    
    for char in s:
        if char.isalpha():
            letters = True
            new_s += char.swapcase()
        else:
            new_s += char
    
    if not letters:
        new_s = new_s[::-1]

    return new_s

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