def numerical_letter_grade(grades):
    """Convert a list of GPAs to a list of corresponding letter grades."""
    letter_grades = []  # Create an empty list to store the letter grades

    for grade in grades:
        if grade == 4.0:
          letter_grades.append('A+')
        elif grade > 3.7:
          letter_grades.append('A')
        elif grade > 3.3:
          letter_grades.append('A-')
        elif grade > 3.0:
          letter_grades.append('B+')
        elif grade > 2.7:
          letter_grades.append('B')
        elif grade > 2.3:
          letter_grades.append('B-')
        elif grade > 2.0:
          letter_grades.append('C+')
        elif grade > 1.7:
          letter_grades.append('C')
        elif grade > 1.3:
          letter_grades.append('C-')
        elif grade > 1.0:
          letter_grades.append('D+')
        elif grade > 0.7:
          letter_grades.append('D')
        elif grade >= 0.0:
          letter_grades.append('D-')
        else:
          letter_grades.append('E')

    return letter_grades

# Testing the function with example input
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