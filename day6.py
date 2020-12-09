import re

inputFile = open("input/day6.txt", "r")
inputLines = inputFile.readlines()

group = ""
answeredYesCount = 0
allAnsweredYesCount = 0

for line in inputLines:
    if line.strip() == "":
        # We get all answers from this Group
        # Look into how many people answered
        # by the number of newlines
        peopleCount = group.count('\n')

        # Look into all questions answered yes from everyone
        # Remove spaces and newlines
        group = group.replace('\n', '').replace('\r', '')
        group.replace(" ", "")
        # Sort the list
        group = sorted(group)
        group = "".join(group)

        # Regex on the letters that have the correct number of occurences
        if peopleCount == 1:
            group = "".join(set(group))
            allAnsweredYesCount += len(group)
        else:
            answerCount = 1
            lastLetter = ""
            for letter in group:
                if lastLetter == letter:
                    answerCount += 1
                lastLetter = letter
                if answerCount == peopleCount:
                    allAnsweredYesCount += 1
                    answerCount = 1
        # Remove duplicate letters
        group = "".join(set(group))
        answeredYesCount += len(group)

        # Now we get through a new group
        group = ""
    else:
        group += line

print("Questions answered yes {}".format(answeredYesCount))
print("Questions all answered yes {}".format(allAnsweredYesCount))

inputFile.close()

# 2984 too high