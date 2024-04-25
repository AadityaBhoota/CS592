# Define the function do_algebra(operator, operand)
def do_algebra(operator, operand):
    # Check the length constraints for operator and operand lists
    if len(operator) != len(operand) - 1:
        raise ValueError("Length of operator list should be one less than the length of operand list")

    if len(operator) < 1 or len(operand) < 2:
        raise ValueError("Operator list should have at least one operator and operand list should have at least two operands.")

    # Step 1: Initialize the result with the first operand
    result = operand[0]

    # Step 2: Loop through the operators and operands together
    for op, num in zip(operator, operand[1:]):
        # Step 3: Update the result based on the operator
        if op == '+':
            result += num
        elif op == '-':
            result -= num
        elif op == '*':
            result *= num
        elif op == '//':
            result //= num
        elif op == '**':
            result **= num

    return result

# Test the function with an example
operator = ['+', '*', '-']
operand = [2, 3, 4, 5]
result = do_algebra(operator, operand)


def check(candidate):

    # Check some simple cases
    assert candidate(['**', '*', '+'], [2, 3, 4, 5]) == 37
    assert candidate(['+', '*', '-'], [2, 3, 4, 5]) == 9
    assert candidate(['//', '*'], [7, 3, 4]) == 8, "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"


check(do_algebra)