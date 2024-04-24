def check_test_score():
    try:
        score = int(input("Enter a number between 0 and 100: "))

        if score >= 60:
            print("Pass")

        else:
            print("Fail")
    
    except ValueError:
        print("Invalid input. Please enter a valid number between 0 and 100.")

# Call the function
check_test_score()