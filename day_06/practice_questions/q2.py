"""
Create a program that takes a student's exam score as input. Classify the student's performance as follows:

- If the score is greater than or equal to 90, print "A"
- If the score is between 80 and 89, print "B"
- If the score is between 70 and 79, print "C"
- If the score is between 50 and 69, print "D"
- If the score is below 50, print "F"
"""

score = float(input("Enter the exam score: "))

if score >= 90:
    print("A")
elif 80 <= score < 90:
    print("B")
elif 70 <= score < 80:
    print("C")
elif 60 <= score < 70:
    print("D")
else:
    print("F")

