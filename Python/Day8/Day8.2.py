f = open("Day8.1Input.txt", "r")
lines = f.read().split("\n")
if len(lines) <= 3:
    raise Exception("No Input Data")
accNumber = 0
all = []
pos = 0
isLoop = []
nopNumbers = []
jmpNumbers = []
x = "yes"

for i in lines:
    all.append(i)


for i in all:
    if i.startswith("nop"):
        nopNumbers.append(i)

    elif i.startswith("jmp"):
        jmpNumbers.append(i)





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


def replacerNop(replace, all):
    x = []
    for e in range(len(all)):
        if all[e].startswith("nop"):
            x.append([all[e], e])

    e = x[replace][1]
    all[e] = all[e].replace("nop", "jmp")
    return all


def replacerJmp(replace, all):
    x = []
    for e in range(len(all)):
        if all[e].startswith("jmp"):
            x.append([all[e], e])

    e = x[replace][1]
    all[e] = all[e].replace("jmp", "nop")
    return all

def isLooped(accNumber, all):
    pos = 0
    isLoop = []
    for i in range(len(all)+1):
        if pos not in isLoop:
            if pos >= len(all):
                print("Terminated Normal")
                print("The answer is : " + str(accNumber))
                return False
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
            return True




for i in range(len(nopNumbers)):
    all = []
    for e in lines:
        all.append(e)
    accNumber = 0
    all = replacerNop(i, all)
    z = isLooped(accNumber, all)
    if z == False:
        break

for i in range(len(jmpNumbers)):
    all = []
    for e in lines:
        all.append(e)
    accNumber = 0
    all = replacerJmp(i, all)
    z = isLooped(accNumber, all)
    if z == False:
        break


