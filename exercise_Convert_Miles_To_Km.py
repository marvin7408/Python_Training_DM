"""
Write a program that reads a mile in a double value from the console, converts it to kilometers, and displays the result. The formula for the conversion is as follows: 1 mile = 1.6 kilometers

Here is a sample run:

Enter miles: 96
96 miles is 153.6 kilometers
"""
#Enter miles
miles = int(input("Enter Miles: "))
#conversion from miles to km
conversion = 1.6*miles
#Print the results
print(miles,"Miles is ", conversion, "kilometers")