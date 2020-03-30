inputList = input("Enter values: ").split(' ')


def unique(list1):
    uniqueList = []

    for x in list1:
        if x not in uniqueList:
            uniqueList.append(x)
    for x in uniqueList:
        print(x, end=' ')


unique(inputList)

