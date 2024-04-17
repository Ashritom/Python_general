x=str(input("enter any string: "))
print(len(x))


"""without using the len function"""



string = input("Enter a string: ")
letter_count = 0  # Initialize the count of letters

for char in string:
    if char.isalpha():  # Check if the character is a letter
        letter_count += 1  # Increment the count if it's a letter

print("Number of letters:", letter_count)
