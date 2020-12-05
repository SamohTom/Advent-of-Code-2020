f = open("Day3.1Input.txt", "r")
line = f.read().split("\n")
if len(line) == 1:
    raise Exception(" No Input Data")
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
all = []
result = 0
for i in range(len(slopes)):
    x = slopes[i][0]
    y = slopes[i][1]
    counter = 0
    while y < len(line):
        while x > len(line[0]) - 1:
            x -= 31
        if line[y][x] == "#":
            counter += 1
        x += slopes[i][0]
        y += slopes[i][1]
    print(counter)
    all.append(counter)
result = all[0]
for i in range(len(all)-1):
    result = result*all[i+1]
print("The answer is : " + str(result))
