import random

rand = []


def randomGenerator():
    global k
    for n in range(19):
        rand.append(random.randint(0, 100))
    print("Generated numbers: ", rand)

    tmp = 0
    for i in range(len(rand)):
        tmp += rand[i]
    print("Average: ", tmp / 20)

    print("Min: ", min(rand))
    print("Max: ", max(rand))

    print("Second min: ", sorted(rand)[1])
    print("Second max: ", sorted(rand)[-2])

    k = 0
    for i in range(len(rand)):
        if rand[i] % 2 == 0:
            k += 1
    print("Amount of even numbers: ", k)


randomGenerator()
