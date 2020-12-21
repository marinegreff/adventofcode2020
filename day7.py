inputFile = open("input/day7.txt", "r")
inputLines = inputFile.readlines()

listBagsWithoutShinyGold = []
listBagsWithShinyGold = []
listUncertain = []

def goldMiner():
    for line in inputLines:
        splittedLine = line.split()
        bagColor = splittedLine[0] + splittedLine[1]
        childrenBags = []

        if splittedLine[4] == "no" or bagColor == "shinygold":
            if bagColor not in listBagsWithoutShinyGold:
                listBagsWithoutShinyGold.append(bagColor)
        else:
            someChildrenBags = True
            counter = 5
            while someChildrenBags:
                childrenBags.append(splittedLine[counter] + splittedLine[counter + 1])
                if (splittedLine[counter + 2] == "bag.") or (splittedLine[counter + 2] == "bags."):
                    someChildrenBags = False
                counter = counter + 4
            if "shinygold" in childrenBags:
                if bagColor not in listBagsWithShinyGold:
                    listBagsWithShinyGold.append(bagColor)
            else:
                # Look into every children to see if they can have the bag
                for childrenBag in childrenBags:
                    if childrenBag in listBagsWithShinyGold:
                        if bagColor not in listBagsWithShinyGold:
                            listBagsWithShinyGold.append(bagColor)
                    else:
                        if bagColor not in listUncertain:
                            listUncertain.append(bagColor)

goldMiner()
lastRunCount = 0
while lastRunCount != len(listBagsWithShinyGold):
    lastRunCount = len(listBagsWithShinyGold)
    goldMiner()

print("Bags that can eventually contain one shiny gold bag {}".format(len(listBagsWithShinyGold)))

def bagCounter(color):
    for line in inputLines:
        splittedLine = line.split()
        bagColor = splittedLine[0] + splittedLine[1]
        
        if bagColor == color:
            childrenBags = []
            someChildrenBags = True
            counter = 4
            while someChildrenBags:
                childrenBags.append((splittedLine[counter + 1] + splittedLine[counter + 2], int(splittedLine[counter])))
                if (splittedLine[counter + 3] == "bag.") or (splittedLine[counter + 3] == "bags."):
                    someChildrenBags = False
                counter = counter + 4
            return childrenBags
            
numberOfBags = 0
returnedBag = bagCounter("shinygold")
for bag in returnedBag:
    numberOfBags = numberOfBags + bag[1]
    # Need to go down further



print("Nested bags {}".format(numberOfBags))
inputFile.close()
