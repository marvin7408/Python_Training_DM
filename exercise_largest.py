"""Write a program that asks the user to enter three numbers. The program will then determine and print the largest of the three numbers.

Example:

first number? 2
second number? 7
third number? 4

Largest: 7"""

# Variable enter first numnber
FirstNumber = int(input("First numner? "))
#Varible enter second number
SecondNumber = int(input("Second number? "))
#Varible enter third number
ThirdNumber = int(input("Third number? "))

#Check which number is the largest
largest = FirstNumber
if SecondNumber > largest:
    largest = SecondNumber

if ThirdNumber > largest:
    largest = ThirdNumber

# Print the results
print("Largest: ", largest)