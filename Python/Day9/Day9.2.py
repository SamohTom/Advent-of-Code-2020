f = open("Day9.1Inuput.txt", "r")
lines = f.read().split("\n")
if len(lines) <= 3:
    raise Exception("No Input Data")
all = lines[25:]
preamble = lines[:25]
valid = False
number = 0
x = True
sum = []
h = 0

def getSum(sum):
    y = 0
    for i in sum:
        y += int(i)
    return y

def highest(sum):
    max = 0
    for i in sum:
        if int(i) > max:
            max = int(i)
    min = max
    for i in sum:
        if int(i) < min:
            min = int(i)
    z = min+max
    return z

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
        number = int(i)
        break



for i in range(len(lines)):
    if int(lines[i]) == number:
        h = i

all = lines[:h]

while x == True:
    sum = []
    for i in all:
        sum.append(int(i))
        if getSum(sum) == number:
            print("The answer is : " + str(highest(sum)))
            x = False
            break
    all.remove(all[0])

