f = open("Day2.1Input.txt", "r")
line = f.read().split("\n")
if len(line) == 1:
    raise Exception(" No Input Data")
col = []
counter = 0
for i in range(len(line)):
    col = []
    col = line[i].split(" ")
    minMax = col[0].split("-")
    key = col[1].split(":")
    pw = col[2]
    countedLetters = pw.count(key[0])
    if int(minMax[0]) <= countedLetters <= int(minMax[1]):
        counter += 1
        print(line[i])
print("The answer is : " + (counter))