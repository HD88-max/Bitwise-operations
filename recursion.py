def input_until_negative():
    number = int(input("Enter a number (negative number to stop): "))

    if number < 0:
        print("Stopped because a negative number was entered.")
        return
    else:
        print("You entered:", number)
        input_until_negative()

input_until_negative()
