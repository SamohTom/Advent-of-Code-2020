f = open("Day3.1Input.txt", "r")
line = f.read().split("\n")
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
