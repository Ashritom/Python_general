""""
there is no built-in function to reverse a string in Python like strrev in C. However, you can use slicing with a negative step to reverse a string, like this:

string[::-1]

This will return a reversed copy of the string. For example:

"python"[::-1] will return "nohtyp"

"""


x=str(input('enter a string: '))
print(x)
print(x[::-1])

