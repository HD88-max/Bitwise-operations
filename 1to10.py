def onetoten(n):

    if(n>10):
        return
    
    print(n)


    onetoten(n+1)

userinput = int(input("Enter a number that is lower than 10: "))
onetoten(userinput)