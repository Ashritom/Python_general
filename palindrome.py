def palindrome():
    x=input("Enter a string: ")
    if x==x[::-1]:
        print("palindrome")
    else:
        print("not a palindrome")

def main():
    palindrome()
main()