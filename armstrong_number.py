x=int(input("Enter a number : "))
count = 0
temp = x
sum = 0
while(x>0):
    x=x//10
    count = count + 1
x=temp
while(x!=0):
    r = x%10
    sum = sum + (r**count)
    x = x//10

if sum == temp :
    print("Armstrong Number")
else :
    print("Not an Armstrong Number")