n = int(input("Enter a number: "))

position = 1
while n > 0:
    if n & 1 == 1:
        print("Position of rightmost set bit:", position)
        break
    n = n >> 1
    position += 1
