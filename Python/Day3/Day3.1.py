f = open("Day3.1Input.txt", "r")
line = f.read().split("\n")
if len(line) == 1:
    raise Exception(" No Input Data")
x = 3
y = 1
counter = 0
while y < len(line):
    while x > len(line[0]) - 1:
        x -= 31
    if line[y][x] == "#":
        counter += 1
    x += 3
    y += 1
print("The answer is : " + str(counter))
