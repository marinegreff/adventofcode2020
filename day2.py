import re

inputFile = open("input/day2.txt", "r")
inputLines = inputFile.readlines()
regex = '([0-9]*)-([0-9]*) ([a-z]): ([a-z]*)'
numberOfValidPasswords = 0
numberOfReevaluatedValidPasswords = 0

# Loop through the lines 
for line in inputLines:
    # Get the password rules
    minValue = int(re.search(regex, line).group(1))
    maxValue = int(re.search(regex, line).group(2))
    characterToFind = str(re.search(regex, line).group(3))
    passwordToVerify = re.search(regex, line).group(4)
    # Count how much characters is in the password
    foundCharacters = passwordToVerify.count(characterToFind)
    if foundCharacters in range(minValue,maxValue + 1):
        numberOfValidPasswords += 1
    # Part 2, evaluate if the character is either on minValue spot or maxValue spot in the password
    minValue -= 1
    maxValue -= 1
    if len(passwordToVerify) >= maxValue:
        char1 = str(passwordToVerify[minValue])
        char2 = str(passwordToVerify[maxValue])
        print("line: {}".format(line))
        print("char1: {} char2: {}".format(char1, char2))
        if ((char1 == characterToFind) ^ (char2 == characterToFind)):
            numberOfReevaluatedValidPasswords += 1

print("Number of valid passwords: {}".format(numberOfValidPasswords))
print("Number of reevaluated valid passwords: {}".format(numberOfReevaluatedValidPasswords))

inputFile.close()
