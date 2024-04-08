number = int(input("Enter a number: "))
n = number # a variable to do calculations with
total = 1

if number < 0:
    print("Please enter a positive number")
else:
    while True:
        total *= n % 10
        if n < 10:
            break
        n //= 10
        print(total, n)
    print("The multiplication of all digits in", number, "is", total)