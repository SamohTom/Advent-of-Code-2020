f = open("Day4.1Input.txt ", "r")
lines = f.read().split("\n\n")
if len(lines) == 1:
    raise Exception(" No Input Data")

passports = []
passport = []
counter = 0
attr = []
for i in range(len(lines)):
    x = lines[i].replace("\n", " ")
    passports.append(x)

for i in range(len(passports)):
    passport = passports[i].split(" ")
    if len(passport) == 8:
        counter += 1
        print(passports[i])
    elif len(passport) == 7:
        for z in range(len(passport)):
            x = passport[z].split(":")[0]
            attr.append(x)
        if not "cid" in attr:
            counter += 1
            print(passports[i])
        attr = []

print("The answer is : " + str(counter))