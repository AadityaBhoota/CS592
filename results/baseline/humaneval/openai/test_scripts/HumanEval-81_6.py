def numerical_letter_grade(grades):
    def gpa_to_letter(gpa):
        if gpa == 4.0:
            return 'A+'
        elif gpa > 3.7:
            return 'A'
        elif gpa > 3.3:
            return 'A-'
        elif gpa > 3.0:
            return 'B+'
        elif gpa > 2.7:
            return 'B'
        elif gpa > 2.3:
            return 'B-'
        elif gpa > 2.0:
            return 'C+'
        elif gpa > 1.7:
            return 'C'
        elif gpa > 1.3:
            return 'C-'
        elif gpa > 1.0:
            return 'D+'
        elif gpa > 0.7:
            return 'D'
        elif gpa >= 0.0:
            return 'D-'
        else:
            return 'E'

    return [gpa_to_letter(gpa) for gpa in grades]

# Test the function
grades = [4.0, 3, 1.7, 2, 3.5]


def check(candidate):

    # Check some simple cases
    assert candidate([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'B', 'C-', 'C', 'A-']
    assert candidate([1.2]) == ['D+']
    assert candidate([0.5]) == ['D-']
    assert candidate([0.0]) == ['E']
    assert candidate([1, 0.3, 1.5, 2.8, 3.3]) == ['D', 'D-', 'C-', 'B', 'B+']
    assert candidate([0, 0.7]) == ['E', 'D-']

    # Check some edge cases that are easy to work out by hand.
    assert True


check(numerical_letter_grade)