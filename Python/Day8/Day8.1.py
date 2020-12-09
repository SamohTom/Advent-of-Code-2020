f = open("Day8.1Input.txt", "r")
lines = f.read().split("\n")
if len(lines) <= 3:
    raise Exception("No Input Data")
accNumber = 0
all = []
pos = 0
isLoop = []
x = "yes"
for i in lines:
    all.append(i)

def acc(accValue, accNum):
    if accValue.startswith("-"):
        accNum -= int(accValue.replace("-", ""))
        return int(accNum)
    if accValue.startswith("+"):
        accNum += int(accValue.replace("+", ""))
        return int(accNum)
def jmp(jmpValue, pos):
    if jmpValue.startswith("-"):
        pos -= int(jmpValue.replace("-", ""))
        return pos
    if jmpValue.startswith("+"):
        pos += int(jmpValue.replace("+", ""))
        return pos

while x == "yes":
    if pos not in isLoop:
        i = all[pos]
        if i.startswith("acc"):
            accNumber = acc(i.replace("acc ", ""), accNumber)
            isLoop.append(pos)
            pos += 1
        if i.startswith("jmp"):
            isLoop.append(pos)
            z = jmp(i.replace("jmp ", ""), pos)
            if z != 0:
                isLoop.append(pos)
            pos = z
        if i.startswith("nop"):
            isLoop.append(pos)
            pos += 1
    else:
        x = "no"
print("The answer is : " + str(accNumber))
