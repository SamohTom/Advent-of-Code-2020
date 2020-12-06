f = open("Day6.1Input.txt ", "r")
lines = f.read().split("\n\n")
if len(lines) <= 3:
    raise Exception("No Input Data")
counter = 0
letters = []
for i in lines:
    letters = []
    x = i.replace("\n", "")
    y = list(x)
    for z in y:
        if z not in letters:
            letters.append(z)
    counter += len(letters)
print(counter)
