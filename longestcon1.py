def longest_consecutive_ones(n):
    count = 0
    while n:
        n = n & (n << 1)
        count += 1
    return count

userinput = int(input("Enter your number: "))
print(longest_consecutive_ones(userinput))