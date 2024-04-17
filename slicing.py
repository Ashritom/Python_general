x=str(input('enter a string: '))
print(x)
print(x[::-1])
print(x[::-2])
print(x[1::-3])
print(x[:1:-1])
print(x[1::])
print(x[:1:])
print('\n')
""" 
syntax ===>  [start : stop : step]

in the step, if +ve number is givern then the printing starts from 0th index to x index(normally from left to right)...
             if -ve number is givern then the printing starts from x index to 0th index(reverse from right to left)...
"""

sequence = "ABCDEFG"
print(sequence[1:4])     # Output: BCD (starts at index 1, stops before index 4)
print(sequence[:3])      # Output: ABC (starts at the beginning, stops before index 3)
print(sequence[2:])      # Output: CDEFG (starts at index 2, goes to the end)
print(sequence[::2])     # Output: ACEG (starts at the beginning, goes to the end, with a step of 2)
print(sequence[::-1])    # Output: GFEDCBA (reverses the sequence)
print(sequence[4:1:-1])  # Output: EDC (starts at index 4, stops before index 1, with a step of -1)
