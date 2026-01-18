import math

def printPowerSet(arr, setSize):

    powerSetSize = int(math.pow(2,setSize))

    for outer in range(powerSetSize):
        for inner in range(setSize):
            if (outer & (1 << inner)) > 0:
                print(arr[inner], end=" ")
        print()


size = int(input("Enter arry size: "))

arr = []

for i in range(size):
    n = int(input("Enter element: "))
    arr.append(n)

printPowerSet(arr, len(arr))