#static and basic method
a=10
b=20
print("The value of a and b are %d and %d " %(a,b))
print("\n")

#Dynamic method

x=int(input("Enter the value of x: "))
y=int(input("Enter the value of y: "))
print("The value of x and y are {x} and {y}".format(x=x,y=y))
print("\n")

#Dynamic method and also taking input for more than 1 variable in a single line ( using of map and split function)

u,v=map(int,input("Enter the values of u and v: ").split())
print("The value of u and v are {} and {}".format(u,v))
print("\n")


