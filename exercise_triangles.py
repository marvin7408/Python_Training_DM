"""Write a program that reads the lengths of the two sides of a right triangle and calculates the length of the third side. 
Hint: if the first side is a and the second side is b, the third side c is the square root of (a x a) + (b x b).

Note: I did not teach you how to calculate a square root in Python.. Try to search for that yourself!

Example output:

First side: 3
Second side: 4

The length of the third side of this triangle is 5.0"""

# Importing math module to use square root function
import math

# Function to calculate the length of the third side
def calculate_third_side(a, b):
    return math.sqrt(a**2 + b**2)

# Main function
def main():
    # Getting input for the lengths of the first and second sides
    a = float(input("First side: "))
    b = float(input("Second side: "))

    # Calculating the length of the third side
    c = calculate_third_side(a, b)

    # Output the result
    print(f"The length of the third side of this triangle is {c}.")

# Calling the main function
if __name__ == "__main__":
    main()