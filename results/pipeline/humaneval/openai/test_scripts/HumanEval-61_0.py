def correct_bracketing(brackets: str):
    """Check if every opening bracket has a corresponding closing bracket."""
    
    count = 0  # Variable to keep track of the balance of brackets

    for bracket in brackets:  # Iterate over each character in the brackets string
        if bracket == "(":  # If the character is an opening bracket
            count += 1  # Increment the count by 1
        else:  # If the character is a closing bracket
            if count > 0:  # If there are corresponding opening brackets
                count -= 1  # Decrement the count by 1
            else:  # If there is a closing bracket without an opening bracket
                return False  # Return False

    return count == 0



METADATA = {}


def check(candidate):
    assert candidate("()")
    assert candidate("(()())")
    assert candidate("()()(()())()")
    assert candidate("()()((()()())())(()()(()))")
    assert not candidate("((()())))")
    assert not candidate(")(()")
    assert not candidate("(")
    assert not candidate("((((")
    assert not candidate(")")
    assert not candidate("(()")
    assert not candidate("()()(()())())(()")
    assert not candidate("()()(()())()))()")


check(correct_bracketing)