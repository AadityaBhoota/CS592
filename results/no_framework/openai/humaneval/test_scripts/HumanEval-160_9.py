def do_algebra(operators, operands):
    if len(operators) != len(operands) - 1:
        raise ValueError("Invalid input: Number of operators should be one less than the number of operands.")

    result = operands[0]
    for i in range(len(operators)):
        op = operators[i]
        operand = operands[i + 1]

        if op == '+':
            result += operand
        elif op == '-':
            result -= operand
        elif op == '*':
            result *= operand
        elif op == '//':
            result //= operand
        elif op == '**':
            result **= operand
        else:
            raise ValueError("Invalid operator: Supported operators are '+', '-', '*', '//', '**'.")

    return result

# Test the function
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