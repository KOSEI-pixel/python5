def check_age():
    try:
        age = int(input("Enter your age: "))
        if 10 <= age <= 20:
            print("Age is between 10 and 20 years.")
        else:
            print("Age is not between 10 and 20 years.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    check_age()