f = open("Day2.1Input.txt", "r")
line = f.read().split("\n")
col = []
counter = 0
for i in range(len(line)):
    col = []
    col = line[i].split(" ")
    MinMax = col[0].split("-")
    key = col[1].split(":")
    pw = col[2]
    cl = pw.count(key[0])
    if int(MinMax[0]) <= cl <= int(MinMax[1]):
        counter += 1
        print(line[i])
print(counter)