def multiply_digits(n):
    product = 1
    while n > 0:
        digit = n % 10  # Extract the last digit
        product *= digit  # Multiply the digit with the product
        n //= 10  # Remove the last digit
    return product

def main():
    try:
        num = int(input("Enter a number between 0 and 1000: "))
        if 0 <= num <= 1000:
            result = multiply_digits(num)
            print(f"The multiplication of all digits in {num} is {result}.")
        else:
            print("Please enter a valid number between 0 and 1000.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()