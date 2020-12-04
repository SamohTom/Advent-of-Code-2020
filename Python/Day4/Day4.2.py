passports = []
passport = []
attr = {}
attr1 = []
valid = []
validCounter = 0
counter = 0



def attributes(passport):
    for z in range(len(passport)):
        x = passport[z].split(":")[0]
        y = passport[z].split(":")[1]
        attr[x] = y
    return attr

def byrValid(byr):
    if 1920 <= int(byr) <= 2002:
        return True
    else:
        print("byr invalid!")
        return False

def iyrValid(iyr):
    if 2010 <= int(iyr) <= 2020:
        return True
    else:
        print("iyr invalid!")
        return False

def eyrValid(eyr):
    if 2020 <= int(eyr) <= 2030:
        return True
    else:
        print("eyr invalid!")
        return False

def hgtValid(hgt):
    if str(hgt).endswith("cm"):
        hgt = str(hgt).replace("cm", "")
        if 150 <= int(hgt) <= 193:
            return True
        else:
            print("hgt invalid!")
            return False
    elif str(hgt).endswith("in"):
        hgt = str(hgt).replace("in", "")
        if 59 <= int(hgt) <= 76:
            return True
        else:
            print("hgt invalid!")
            return False
    else:
        print("hgt invalid!")
        return False

def hclValid(hcl):
    f = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    c = False
    if str(hcl).startswith("#"):
        hcl = list(str(hcl).replace("#", ""))
        for i in range(len(hcl)):
            if hcl[i] in f:
                c = True
            else:
                print("hcl invalid!")
                return False
                break
        if c:
            return True

    else:
        print("hcl invalid!")
        return False

def eclValid(ecl):
    f = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if str(ecl) in f:
        return True
    else:
        print("ecl invalid!")
        return False

def pidValid(pid):
    if len(pid) == 9:
        try:
            int(pid)
            return True
        except:
            print("pid invalid!")
            return False
    else:
        print("pid invalid!")
        return False


f = open("Day4.1Input.txt ", "r")
lines = f.read().split("\n\n")

for i in range(len(lines)):
    x = lines[i].replace("\n", " ")
    passport.append(x)

for i in range(len(passport)):
    x = passport[i].split(" ")
    passports.append(x)


for i in range(len(passports)):
    if len(passports[i]) == 8:
        valid.append(passports[i])
        validCounter += 1
    elif len(passports[i]) == 7:
        attr = {}
        attr = attributes(passports[i])
        if not "cid" in attr.keys():
            valid.append(passports[i])
            validCounter += 1




for i in range(len(valid)):
    attr = attributes(valid[i])
    if byrValid(attr["byr"]) and iyrValid(attr["iyr"]) and eyrValid(attr["eyr"]) and hgtValid(attr["hgt"]) and hclValid(attr["hcl"]) and eclValid(attr["ecl"]) and pidValid(attr["pid"]):
        counter += 1
print("The answer is : " + str(counter))



