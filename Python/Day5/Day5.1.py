f = open("Day5.1Input.txt ", "r")
lines = f.read().split("\n")
if len(lines) == 1:
    raise Exception(" No Input Data")

rows = 128
columns = 8
row = []
highest = 0
currentRow = []
currentColumn = []


def front(currentRow):
    x = int(len(currentRow)/2)
    z = currentRow[x:]
    for i in z:
        currentRow.remove(i)
    return currentRow

def back(currentRow):
    x = int(len(currentRow)/2)
    z = currentRow[:x]
    for i in z:
        currentRow.remove(i)
    return currentRow

def left(currentColumn):
    x = int(len(currentColumn)/2)
    z = currentColumn[x:]
    for i in z:
        currentColumn.remove(i)
    return currentColumn

def right(currentColumn):
    x = int(len(currentColumn)/2)
    z = currentColumn[:x]
    for i in z:
        currentColumn.remove(i)
    return currentColumn



for i in range(len(lines)):
    x = list(lines[i])
    row.append(x)

for i in range(len(row)):
    currentColumn = []
    currentRow = []
    for x in range(rows):
        currentRow.append(x)
    for x in range(columns):
        currentColumn.append(x)
    for z in range(len(row[i])):
        if row[i][z] == "F":
            x = front(currentRow)
            currentRow = x
        if row[i][z] == "B":
            x = back(currentRow)
            currentRow = x
        if row[i][z] == "L":
            x = left(currentColumn)
            currentColumn = x
        if row[i][z] == "R":
            x = right(currentColumn)
            currentColumn = x
    y = (currentRow[0]*8)+currentColumn[0]
    if y > highest:
        highest = y
print("The answer is : " + str(highest))