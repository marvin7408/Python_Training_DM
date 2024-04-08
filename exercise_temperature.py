"""Write a program that asks the user to enter a temperature in degrees Celsius.
The program will convert the temperature to degrees Fahrenheit and display the result to the user with an appropriate message.
(Hint: F° = (1.8 × C°) + 32.)

Example output:

Enter a temperature in Celsius? 40

That is 104.0 degrees Fahrenheit.
"""

#input temperature
temp = int(input("Enter a temperature in Celsius? "))

#Print the conversion to Fahrenheit to the screen. Math for corversion from temp to F (1.8*C)+32)
print("That is", 1.8*temp+32, "degrees Fahrenheit.")