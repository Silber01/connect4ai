import json


def printBitified(bitified):
    for i in range(5, -1, -1):
        print("|", end="  ")
        for j in range(6, -1, -1):
            print("X" if (bitified & (2 ** ((7 * i) + (6 - j))) > 0) else ".", end="  ")
        print("|")


def makeSolution(bits, solutions, forms):
    bitified = (2 ** bits[0] + 2 ** bits[1] + 2 ** bits[2] + 2 ** bits[3])
    forms.append(bitified)
    for b in bits:
        solutions[b] = solutions.get(b, [])
        solutions[b].append(bitified)


def incBits(bits, amnt):
    for i in range(4):
        bits[i] += amnt


def getSolutions():
    solutions = {}
    forms = []

    bits = [0,1,2,3]

    for i in range(6):
        for j in range(4):
            makeSolution(bits, solutions, forms)
            incBits(bits, 1)
        incBits(bits, 3)

    bits = [0, 7, 14, 21]
    for i in range(21):
        makeSolution(bits, solutions, forms)
        incBits(bits, 1)

    bits = [0, 8, 16, 24]
    for i in range(3):
        for j in range(4):
            makeSolution(bits, solutions, forms)
            incBits(bits, 1)
        incBits(bits, 3)

    bits = [3, 9, 15, 21]
    for i in range(3):
        for j in range(4):
            makeSolution(bits, solutions, forms)
            incBits(bits, 1)
        incBits(bits, 3)

    with open("solutions.json", "w") as writeFile:
        json.dump(solutions, writeFile)
    with open("forms.json", "w") as writeFile:
        json.dump({"FORMS": forms}, writeFile)


    for s in solutions:
        print("SOLUTIONS INVOLVING:")
        printBitified(2 ** s)
        print("\n")
        for p in solutions[s]:
            printBitified(p)
            print()
        print("\n\n")