def prime(x):
    
    count=1
    i=2
    
    while i<=x:
        if x%i==0:
           count=count+1
        i=i+1
    
    
    if count==2:
        print("Prime number")
    else:
        print("Not a Prime number")
    


def main():
    x=int(input("Enter the value of x: "))
    prime(x)
main()