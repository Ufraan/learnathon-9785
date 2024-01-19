#> Create a function called **`grade_converter`** that takes a numerical grade as an argument and returns the corresponding letter grade (A, B, C, D, F) based on the standard grading scale.
 
#- If the score is greater than or equal to 90, print "A"
#- If the score is between 80 and 89, print "B"
#- If the score is between 70 and 79, print "C"
#- If the score is between 50 and 69, print "D"
#- If the score is below 50, print "F"


def grade_converter(numerical_grade):
    if numerical_grade >= 90:
        return 'A'
    elif numerical_grade >= 80:
        return 'B'
    elif numerical_grade >= 70:
        return 'C'
    elif numerical_grade >= 50:
        return 'D'
    else:
        return 'F'


letter_grade = grade_converter(85)
print("Letter Grade is : {letter_grade}")
