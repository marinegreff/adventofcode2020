import re

inputFile = open("input/day4.txt", "r")
inputLines = inputFile.readlines()

numberOfValidPassports = 0
passport = ""

# Regexes
countryIdReg = "(cid):([0-9]*)"

for line in inputLines:
    if line.strip() == "":
        # Passport is complete. Search for all fields
        print("Pass: byr {} iyr {} eyr {} hgt {} hcl {} ecl {} pid {}".format(re.search("iyr:[0-9]{4}", passport),re.search("iyr:[0-9]{4}", passport),re.search("eyr:[0-9]{4}", passport),re.search("hgt:[0-9]{2,3}(cm|in)", passport),re.search("hcl:#[a-f0-9]{6}", passport),re.search("ecl:(amb|blu|brn|gry|grn|hzl|oth)", passport),re.search("pid:[0-9]{9}", passport)))
        if (re.search("byr:([0-9]{4})", passport)
                and re.search("iyr:[0-9]{4}", passport)
                and re.search("eyr:[0-9]{4}", passport)
                and re.search("hgt:[0-9]{2,3}(cm|in)", passport)
                and re.search("hcl:#[a-f0-9]{6}", passport)
                and re.search("ecl:(amb|blu|brn|gry|grn|hzl|oth)", passport)
                and re.search("pid:[0-9]{9}", passport)):
            # Extra verificatons
            if (int(re.search("byr:([0-9]{4})", passport).group(1)) in range(1920,2003)
                    and int(re.search("iyr:([0-9]{4})", passport).group(1)) in range(2010, 2021)
                    and int(re.search("eyr:([0-9]{4})", passport).group(1)) in range(2020, 2031)):
                if re.search("hgt:([0-9]{3})cm", passport):
                    if int(re.search("hgt:([0-9]{3})cm", passport).group(1)) in range(150, 194):
                        numberOfValidPassports += 1
                        print("Valid")
                if re.search("hgt:([0-9]{2})in", passport):
                    if int(re.search("hgt:([0-9]{2})in", passport).group(1)) in range(59, 77):
                        numberOfValidPassports += 1
                        print("Valid")
        # Now we get through a new passport
        passport = ""
    else:
        passport += line
        passport += " "


print("Number of valid passports: {}".format(numberOfValidPassports))

inputFile.close()

# entre 130 et 148