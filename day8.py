inputFile = open("input/day8.txt", "r")
inputLines = inputFile.read().splitlines()

accumulator = 0
currentLine = 0
linesAlreadyRead = []

while currentLine not in linesAlreadyRead:
    # Read the current line
    instruction  = inputLines[currentLine]
    linesAlreadyRead.append(currentLine)
    print("Instruction {} Line {}".format(instruction[0:3], currentLine))

    if instruction[0:3] == 'nop':
        # Pass to the line immediately after without doing anything
        currentLine = currentLine + 1
    elif instruction[0:3] == 'acc':
        # Increase or decrease the accumulator
        if instruction[4:5] == '+':
            accumulator = accumulator + int(instruction[5:])
        else:
            accumulator = accumulator - int(instruction[5:])
        # Pass on to the next line
        currentLine = currentLine + 1
    elif instruction[0:3] == 'jmp':
        # Jump to the desired line
        if instruction[4:5] == '+':
            currentLine = currentLine + int(instruction[5:])
        else:
            currentLine = currentLine - int(instruction[5:])


print("Accumulator {}".format(accumulator))
inputFile.close()