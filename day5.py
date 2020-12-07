inputFile = open("input/day5.txt", "r")
inputLines = inputFile.readlines()

highestSeatId = 0
listSeatId = []

def findSeat(line):
    index = 0
    rowList = range(0, 128)
    seatList = range(0, 8)

    while index < len(line):
        if line[index] == "F":
            rowList = rowList[:len(rowList)//2]
        elif line[index] == "B":
            rowList = rowList[len(rowList)//2:]
        elif line[index] == "L":
            seatList = seatList[:len(seatList)//2]
        elif line[index] == "R":
            seatList = seatList[len(seatList)//2:]
        index += 1
    return rowList, seatList

for line in inputLines:
    rowSeatTuple = findSeat(line.strip())
    seatId = (int(rowSeatTuple[0][0]) * 8) + int(rowSeatTuple[1][0])
    #print("line {} rowSeatTuple {} seatId {}".format(line, rowSeatTuple, seatId))
    listSeatId.append(int(seatId))
    if seatId > highestSeatId:
        highestSeatId = seatId
    

emptySeats = [seat for seat in range(80,max(listSeatId)+1) if seat not in listSeatId]

print("The highest seat ID is {}".format(highestSeatId))
print("The list of missing seats : {}".format(emptySeats)) 

inputFile.close()