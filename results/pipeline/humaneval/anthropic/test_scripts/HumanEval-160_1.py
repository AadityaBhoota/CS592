def do_algebra(operator, operand):
    if len(operator) != len(operand) - 1:
        raise ValueError("Length of operator list should be equal to length of operand list minus one.")
    if len(operator) < 1:
        raise ValueError("Operator list should have at least one operator.")
    if len(operand) < 2:
        raise ValueError("Operand list should have at least two operands.")
    if any(not isinstance(x, int) or x < 0 for x in operand):
        raise ValueError("Operand list should contain only non-negative integers.")

    result = operand[0]

    for i, op in enumerate(operator):
        if op == "+":
            result += operand[i + 1]
        elif op == "-":
            result -= operand[i + 1]
        elif op == "*":
            result *= operand[i + 1]
        elif op == "//":
            result //= operand[i + 1]
        elif op == "**":
            result **= operand[i + 1]
        else:
            raise ValueError(f"Invalid operator: {op}")

    return result

def check(candidate):

    # Check some simple cases
    assert candidate(['**', '*', '+'], [2, 3, 4, 5]) == 37
    assert candidate(['+', '*', '-'], [2, 3, 4, 5]) == 9
    assert candidate(['//', '*'], [7, 3, 4]) == 8, "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"


check(do_algebra)