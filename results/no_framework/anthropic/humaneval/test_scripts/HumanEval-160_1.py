def do_algebra(operator, operand):
    """
    Given two lists operator, and operand. The first list has basic algebra operations, and 
    the second list is a list of integers. Use the two given lists to build the algebric 
    expression and return the evaluation of this expression.

    The basic algebra operations:
    Addition ( + ) 
    Subtraction ( - ) 
    Multiplication ( * ) 
    Floor division ( // ) 
    Exponentiation ( ** ) 

    Example:
    operator['+', '*', '-']
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    => result = 9

    Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.

    """
    # Verify the input lists
    if len(operator) != len(operand) - 1:
        raise ValueError("The length of operator list must be equal to the length of operand list minus one.")
    
    if any(num < 0 for num in operand):
        raise ValueError("Operand list must contain non-negative integers.")
    
    if len(operator) < 1 or len(operand) < 2:
        raise ValueError("Operator list must have at least one operator, and operand list must have at least two operands.")
    
    # Perform the algebraic operations
    result = operand[0]
    for i in range(len(operator)):
        if operator[i] == "+":
            result += operand[i+1]
        elif operator[i] == "-":
            result -= operand[i+1]
        elif operator[i] == "*":
            result *= operand[i+1]
        elif operator[i] == "//":
            result //= operand[i+1]
        elif operator[i] == "**":
            result **= operand[i+1]
        else:
            raise ValueError(f"Invalid operator: {operator[i]}")
    
    return result

def check(candidate):

    # Check some simple cases
    assert candidate(['**', '*', '+'], [2, 3, 4, 5]) == 37
    assert candidate(['+', '*', '-'], [2, 3, 4, 5]) == 9
    assert candidate(['//', '*'], [7, 3, 4]) == 8, "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"


check(do_algebra)