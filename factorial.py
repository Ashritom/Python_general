num=int(input("Enter a number: "))
fact=1
temp=num
while temp!=0:
    fact=fact*temp
    temp=temp-1

print("factorial of {} is {}".format(num,fact))



""" num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial:", factorial)
"""
