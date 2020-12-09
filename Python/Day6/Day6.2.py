f = open("Day6.1Input.txt", "r")
lines = f.read().split("\n\n")
if len(lines) <= 3:
    raise Exception("No Input Data")
counter = 0
letters = []
key = ""
for i in lines:
    letters = []
    x = i.split("\n")
    for z in x:
        letters += (list(z))
    while 0 < len(letters):
        key = letters[0]
        if letters.count(key) == len(x):
            counter += 1
        for y in range(letters.count(letters[0])):
            letters.remove(key)
print("The answer is : " + str(counter))
