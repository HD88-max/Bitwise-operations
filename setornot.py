def IsSetOrNot(n):
    ones = 0
    zeros = 0
    while(n):
        if(n &1 == 1):
            ones += 1
            
        else:
            zeros += 1
        n >>= 1
    print("Number of ones:", ones, "Number of zeros:", zeros)

number = int(input(" Enter a number: "))
IsSetOrNot(number)