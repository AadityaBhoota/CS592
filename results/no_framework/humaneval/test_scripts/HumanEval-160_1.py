def do_algebra(operators, operands):
    expression = str(operands[0])
    for i in range(len(operators)):
        expression += ' ' + operators[i] + ' ' + str(operands[i + 1])

    return eval(expression)

# Example usage
operators = ['+', '*', '-']
operands = [2, 3, 4, 5]
result = do_algebra(operators, operands)


def check(candidate):

    # Check some simple cases
    assert candidate(['**', '*', '+'], [2, 3, 4, 5]) == 37
    assert candidate(['+', '*', '-'], [2, 3, 4, 5]) == 9
    assert candidate(['//', '*'], [7, 3, 4]) == 8, "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"


check(do_algebra)