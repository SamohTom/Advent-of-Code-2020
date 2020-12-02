f = open("Day2.1Input.txt", "r")
line = f.read().split("\n")
col = []
counter = 0
for i in range(len(line)):
    col = []
    col = line[i].split(" ")
    pos = col[0].split("-")
    key = col[1][0]
    pw = col[2]
    p1 = pw[int(pos[0])-1]
    p2 = pw[int(pos[1])-1]
    if p1 == key:
        if p2 != key:
            counter += 1
            print(line[i])
    else:
        if p2 == key[0]:
            counter += 1
            print(line[i])
print(counter)