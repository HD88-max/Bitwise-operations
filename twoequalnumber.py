def check_if_same(number1, number2):
    if(number1 ^ number2)!= 0:
        print("Numbers are not equal. ")
    else:
        print("Numbers are equal. ")


number1 = int(input("Enter your first number: "))
number2 = int(input("Enter your second number: "))

check_if_same(number1,number2)