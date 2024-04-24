def do_algebra(operator, operand):
    if len(operator) != len(operand) - 1:
        return "Invalid input: Length of the operator list should be one less than the length of the operand list"

    result = operand[0]

    for i in range(len(operator)):
        op = operator[i]
        num = operand[i + 1]
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
        else:
            return "Invalid input: Unsupported operator"

    return result

# Example usage
operators = ['+', '*', '-']
operands = [2, 3, 4, 5]
print(do_algebra(operators, operands))  # Output: 9

def check(candidate):

    # Check some simple cases
    assert candidate(['**', '*', '+'], [2, 3, 4, 5]) == 37
    assert candidate(['+', '*', '-'], [2, 3, 4, 5]) == 9
    assert candidate(['//', '*'], [7, 3, 4]) == 8, "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"


check(do_algebra)