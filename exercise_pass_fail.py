"""Ask the user to enter a test score (a number between 0 and 100).
If it is 60 or higher, print "Pass", else print "Fail
"""

score = int(input("Enter a number between 0 and 100: "))

if score >= 60:
    print("Pass")

else:
    print("Fail")