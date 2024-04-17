'''
import math
x=144
print(int(math.sqrt(x)))

set={5,78,63,42,98,128,65,45,5}
print(set)

list=[5,78,63,42,98,128,65,45,5]
print(list)

tupple=(5,78,63,42,98,128,65,45,5)
print(tupple)

'''



'''
x = [1, 2, 3]
y = x
x += [4]
print(y)


a = [1, 2, 3]
b = a
a = a + [4]
print(b)
'''


x = 10
y = 20

condition = y > x
result_1 = int(condition)
result_2 = condition

print("Result 1 is %d" % result_1)  # Output: Result 1 is 1 or Result 1 is 0
print("Result 2 is %r" % result_2)  # Output: Result 2 is True or Result 2 is False
