inputFile = open("input/day1.txt", "r")

expenseLines = inputFile.readlines()

# Loop through the lines 
for expense1 in expenseLines:
    # Cleans the newline character
    number1 = int(expense1.strip())
    for expense2 in expenseLines:
        # Cleans the newline character
        number2 = int(expense2.strip())
        # Let's find All possibilities now
        if (number1 + number2) == 2020:
            print("Found two number that sums 2020: {} {}".format(number1, number2))
            print("Multiplied them together: {}".format(number1 * number2))
        for expense3 in expenseLines:
            # Cleans the newline character
            number3 = int(expense3.strip())
            # Let's find All possibilities now for part two
            if(number1 + number2 + number3) == 2020:
                print("Part 2: Found three number that sums 2020: {} {} {}".format(number1, number2, number3))
                print("Multiplied them together: {}".format(number1 * number2 * number3))

inputFile.close()