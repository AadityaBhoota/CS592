def numerical_letter_grade(grades):
    grade_mapping = {
        4.0: 'A+',
        3.7: 'A',
        3.3: 'A-',
        3.0: 'B+',
        2.7: 'B',
        2.3: 'B-',
        2.0: 'C+',
        1.7: 'C',
        1.3: 'C-',
        1.0: 'D+',
        0.7: 'D',
        0.0: 'D-',
        -0.1: 'E'
    }
    
    letter_grades = []
    for grade in grades:
        for cutoff, letter in grade_mapping.items():
            if grade >= cutoff:
                letter_grades.append(letter)
                break
    
    return letter_grades

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