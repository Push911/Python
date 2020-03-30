def column(filename):
    with open(filename, 'r') as file:
        return print("Total amount of bytes:", sum(int(line.split(" ")[-1]) for line in file))


print(column('test.txt'))
