inputFile = open("input/day9.txt", "r")
inputLines = inputFile.readlines()

preambleNumbers = []
invalidNumber = 0

for line in inputLines:
    if len(preambleNumbers) == 25:
        validNumber = False
        for number1 in preambleNumbers:
            for number2 in preambleNumbers:
                if int(line) == number1 + number2:
                    validNumber = True
        if validNumber == False:
            invalidNumber = int(line)
        preambleNumbers.pop(0)
    preambleNumbers.append(int(line))

print("Invalid numbers {}".format(invalidNumber))

# Searching for the encryption weakness
smallestWeakness = 0
biggestWeakness = 0
currentNumber = 0
counter = 0
secondCounter = 0
inputFile = open("input/day9.txt", "r")
inputLines = inputFile.read().splitlines()

while counter < len(inputLines):
    listNumbers = []
    smallestWeakness = int(inputLines[counter])
    listNumbers.append(smallestWeakness)
    currentNumber = smallestWeakness
    secondCounter = counter + 1

    while currentNumber < invalidNumber:
        biggestWeakness = int(inputLines[secondCounter])
        listNumbers.append(biggestWeakness)
        currentNumber = currentNumber + biggestWeakness
        if currentNumber == invalidNumber:
            print("Smallest Weakness {} Biggest Wekness {} Sum {}".format(min(listNumbers), max(listNumbers), min(listNumbers) + max(listNumbers)))
        secondCounter = secondCounter + 1
    counter = counter + 1


inputFile.close()