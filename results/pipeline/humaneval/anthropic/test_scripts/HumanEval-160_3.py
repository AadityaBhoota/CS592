def do_algebra(operator, operand):
    if len(operator) != len(operand) - 1:
        raise ValueError("The length of the operator list must be equal to the length of the operand list minus one.")
    
    for op in operand:
        if op < 0:
            raise ValueError("The operand list must contain only non-negative integers.")
    
    if len(operator) < 1 or len(operand) < 2:
        raise ValueError("The operator list must have at least one operator, and the operand list must have at least two operands.")
    
    result = operand[0]
    
    for i in range(len(operator)):
        if operator[i] == '+':
            result += operand[i+1]
        elif operator[i] == '-':
            result -= operand[i+1]
        elif operator[i] == '*':
            result *= operand[i+1]
        elif operator[i] == '//':
            result //= operand[i+1]
        elif operator[i] == '**':
            result **= operand[i+1]
        else:
            raise ValueError(f"Unknown operator: {operator[i]}")
    
    return result

def check(candidate):

    # Check some simple cases
    assert candidate(['**', '*', '+'], [2, 3, 4, 5]) == 37
    assert candidate(['+', '*', '-'], [2, 3, 4, 5]) == 9
    assert candidate(['//', '*'], [7, 3, 4]) == 8, "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"


check(do_algebra)