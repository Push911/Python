from math import *
x = input("Enter: ")

if '^' in x:
    f = x.replace('^', '**')
    print(eval(f))
else:
    print(eval(x, {'sqrt': sqrt, 'pow': pow, 'sin': sin, 'cos': cos, 'tan': tan, 'atan': atan}))


