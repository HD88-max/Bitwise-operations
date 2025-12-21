def powerofeight(number):
    if number <= 0:
        return False
    if number & (number - 1) != 0:
        return False
    count = 0
    while number > 1:
        number >>= 1
        count += 1

    return count % 3 == 0


number = int(input("Enter a number: "))

if powerofeight(number):
    print(number, "is a power of 8")
else:
    print(number, "isn't a power of 8")