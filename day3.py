inputFile = open("input/day3.txt", "r")
inputLines = inputFile.read().splitlines()

maxX = len(inputLines[0]) - 1
maxY = len(inputLines) - 1

def move(xMov, yMov):
    xPos = 0
    yPos = 0
    treeEncountered = 0
    while yPos <= maxY:
        encountered = inputLines[yPos][xPos]
        if encountered == "#":
            treeEncountered += 1
        xPos = xPos + xMov
        if xPos > maxX:
            xPos = xPos - (maxX + 1)
        yPos = yPos + yMov
    print("Encountered trees: {}".format(treeEncountered))
    return treeEncountered

# Part 1
print("Total encountered trees: {}".format(move(1,1) * move(3,1) * move(5,1) * move(7,1) * move(1,2)))

inputFile.close()