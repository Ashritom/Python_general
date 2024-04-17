def fibonacci():
    n1=0
    n2=1
    x=int(input("enter the value of x: "))
    i=3
    print(n1)
    print(n2)
    while i<=x:
        n3=n1+n2
        print(n3)
        n1=n2
        n2=n3
        i=i+1
fibonacci()