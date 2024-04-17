x = int(input("Enter a number : "))
sum = 0
while(x!=0):
    r = x%10
    sum = sum + r
    x=x//10
print("Sum of the digits of the given number : ",sum)