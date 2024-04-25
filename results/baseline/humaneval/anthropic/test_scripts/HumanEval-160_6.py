def do_algebra(operator, operand):
    """
    Given two lists `operator` and `operand`, the function evaluates the algebraic expression
    formed by applying the operators in `operator` to the operands in `operand`.

    Args:
        operator (list): A list of basic algebra operations ('+', '-', '*', '//', '**').
        operand (list): A list of non-negative integers.

    Returns:
        int: The result of evaluating the algebraic expression.
    """
    if not operator or len(operand) != len(operator) + 1:
        raise ValueError("Invalid input lists. Operator list must be one shorter than the operand list.")

    result = operand[0]
    for i, op in enumerate(operator):
        if op == '+':
            result += operand[i + 1]
        elif op == '-':
            result -= operand[i + 1]
        elif op == '*':
            result *= operand[i + 1]
        elif op == '//':
            result //= operand[i + 1]
        elif op == '**':
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