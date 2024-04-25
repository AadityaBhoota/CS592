def do_algebra(operator, operand):
    if len(operand) < 2 or len(operator) != len(operand) - 1:
        return "Invalid input lists. Operand list must have at least 2 elements, and Operator list length should be 1 less than operand list."

    expression = str(operand[0])
    for i in range(len(operator)):
        expression += operator[i] + str(operand[i + 1])

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