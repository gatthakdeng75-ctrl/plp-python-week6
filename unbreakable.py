def get_number():
    while True:
        try:
            number = int(input("Enter a whole number: "))
            return number
        except ValueError:
            print("Please enter a valid whole number.")


number = get_number()
print(f"You entered: {number}")