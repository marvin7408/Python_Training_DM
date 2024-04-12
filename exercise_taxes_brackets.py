"""Ask the user to input his income in dollars.
Then print how much taxes he has to pay according to the following (imaginary) rules:

Anything below $ 20,000: no taxes
$20,000 - $50,000: 30%
Everything above: 60%"""

#Variable Enter income to determine if taxes need to pay.
income = float(input("Enter income: "))

#If statement to check if the income is less the 20,000. No taxes need to pay.
if income < 20000:
    print("You don't have to pay taxes!")

elif income <=50000:
    print("")