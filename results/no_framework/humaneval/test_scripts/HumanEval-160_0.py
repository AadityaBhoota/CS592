def do_algebra(operators, operands):
    if len(operators) != len(operands) - 1:
        return "Error: Number of operators should be one less than the number of operands."

    if not all(isinstance(op, int) for op in operands):
        return "Error: Operands should be non-negative integers."

    expression = str(operands[0])
    for i in range(len(operators)):
        expression += " " + operators[i] + " " + str(operands[i + 1])

    try:
        result = eval(expression)
        return result
    except Exception as e:
        return "Error: Invalid expression."

# Example usage
operators = ['+', '*', '-']
operands = [2, 3, 4, 5]


def check(candidate):

    # Check some simple cases
    assert candidate(['**', '*', '+'], [2, 3, 4, 5]) == 37
    assert candidate(['+', '*', '-'], [2, 3, 4, 5]) == 9
    assert candidate(['//', '*'], [7, 3, 4]) == 8, "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"


check(do_algebra)