"""Ask the user to enter a test score (a number between 0 and 100).
If it is 60 or higher, print "Pass", else print "Fail
"""

#Variable score with input number between 0 and 100
score = int(input("Enter a number between 0 and 100: "))

#If statement to check if the entered number is equel or greater then 60
if score >= 60:
    print("Pass")

else:
    print("Fail")