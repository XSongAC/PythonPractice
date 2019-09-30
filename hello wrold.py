"""
This is a first hello world python file
I will try to learn python as much as possible
Author: Xiwen
Date: 27 Aug 2019
"""

print('Hello World!')

""" 
import turtle

turtle.pensize(4)
turtle.pencolor('red')
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.mainloop()
"""

a = 5
b = 10
c = 3
d = 4
e = 5
a += b
print("a = ", a)
a -= c
print("a = ", a)
a *= d
print("a = ", a)
a /= e
print("a = ", a)

flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag1
print("flag1 = ", flag1)
print("flag2 = ", flag2)
print("flag3 = ", flag3)
print("flag4 = ", flag4)
print("flag5 = ", flag5)
print(flag1 is True)
print(flag2 is not False)

"""
F = 1.8C + 32
"""
f = float(input('the F degree you enter: '))
c = (f-32)/1.8
print('%.1f Fahrenheit = %.1f Celsius' % (f, c))

