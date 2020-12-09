f = open("Day9.1Inuput.txt", "r")
lines = f.read().split("\n")
if len(lines) <= 3:
    raise Exception("No Input Data")
all = lines[25:]
preamble = lines[:25]
valid = False
for i in all:
    valid = False
    for e in preamble:
        for f in preamble:
            if int(i) == int(e)+int(f):
                if int(f) == int(e):
                    valid = False
                else:
                    valid = True
        if valid:
            break
    preamble.remove(preamble[0])
    preamble.append(i)
    if valid == False:
        print("The answer is : " + str(int(i)))
        break