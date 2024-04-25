import operator

def do_algebra(operator, operand):
    if len(operator) != len(operand) - 1:
        raise ValueError("The length of the operator list must be one less than the length of the operand list.")
    for op in operand:
        if not isinstance(op, int) or op < 0:
            raise ValueError("The operand list must contain only non-negative integers.")
    if len(operator) < 1 or len(operand) < 2:
        raise ValueError("The operator list must have at least one operator and the operand list must have at least two operands.")

    def evaluate(ops, ops_):
        if len(ops) == 0:
            return ops_[0]
        
        op = ops.pop(0)
        op1 = ops_.pop(0)
        op2 = ops_.pop(0)
        
        try:
            if op == '+':
                return evaluate(ops, [operator.add(op1, op2)] + ops_)
            elif op == '-':
                return evaluate(ops, [operator.sub(op1, op2)] + ops_)
            elif op == '*':
                return evaluate(ops, [operator.mul(op1, op2)] + ops_)
            elif op == '//':
                if op2 == 0:
                    raise ZeroDivisionError("Division by zero.")
                return evaluate(ops, [operator.floordiv(op1, op2)] + ops_)
            elif op == '**':
                return evaluate(ops, [operator.pow(op1, op2)] + ops_)
            else:
                raise ValueError(f"Invalid operator: {op}")
        except ZeroDivisionError as e:
            raise e
        except Exception as e:
            raise ValueError(f"Error evaluating expression: {e}")

    return evaluate(operator, operand)

def check(candidate):

    # Check some simple cases
    assert candidate(['**', '*', '+'], [2, 3, 4, 5]) == 37
    assert candidate(['+', '*', '-'], [2, 3, 4, 5]) == 9
    assert candidate(['//', '*'], [7, 3, 4]) == 8, "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"


check(do_algebra)