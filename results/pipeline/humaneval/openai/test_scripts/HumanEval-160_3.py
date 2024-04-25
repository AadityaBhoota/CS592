def do_algebra(operator, operand):
    if len(operator) != len(operand) - 1:
        return "Error: Length of operator list should be one less than the length of the operand list."

    expression = str(operand[0]) 

    for i in range(len(operator)):
        expression += operator[i]  # Add the operator
        expression += str(operand[i+1])  # Add the current operand

    result = eval(expression)

    return result

def check(candidate):

    # Check some simple cases
    assert candidate(['**', '*', '+'], [2, 3, 4, 5]) == 37
    assert candidate(['+', '*', '-'], [2, 3, 4, 5]) == 9
    assert candidate(['//', '*'], [7, 3, 4]) == 8, "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"


check(do_algebra)