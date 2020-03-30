import math

figure = input("Choose figure: ")
i = int(input("Enter number: "))


def square(x):
    area = x * x
    perimeter = 4 * x
    print("Square area: ", area, "\nSquare perimeter: ", perimeter)


def circle(x):
    area = x ** 2 * math.pi
    perimeter = 2 * math.pi * x
    print("Circle area: ", area, "\nCircle perimeter: ", perimeter)


def fig(f):
    if f == 'circle':
        circle(i)
    elif f == 'square':
        square(i)
    else:
        print("Figure not found")


fig(figure)