def poweroffour(number):
    if number < 0:
        return False
    if number &(~(number & (number - 1))):
        count = 0
        while number > 1:
            number >>= 1
            count += 1
        
        if count % 2 == 0:
            return True
        else:
            return False
    
    return False





number = int(input("Enter a number: "))

if poweroffour(number):
    print(number, "is a power of 4")
else:
    print(number, "isn't a power of 4" )    