def numerical_letter_grade(grades):
    letter_grades = []
    for grade in grades:
        if grade >= 4.0:
            letter_grade = 'A+'
        elif grade > 3.7:
            letter_grade = 'A'
        elif grade > 3.3:
            letter_grade = 'A-'
        elif grade > 3.0:
            letter_grade = 'B+'
        elif grade > 2.7:
            letter_grade = 'B'
        elif grade > 2.3:
            letter_grade = 'B-'
        elif grade > 2.0:
            letter_grade = 'C+'
        elif grade > 1.7:
            letter_grade = 'C'
        elif grade > 1.3:
            letter_grade = 'C-'
        elif grade > 1.0:
            letter_grade = 'D+'
        elif grade > 0.7:
            letter_grade = 'D'
        elif grade > 0.0:
            letter_grade = 'D-'
        else:
            letter_grade = 'E'
        letter_grades.append(letter_grade)
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