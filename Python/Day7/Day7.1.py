file = open("Day7.1Input.txt", "r")
lines = file.read().split(".")
if len(lines) <= 3:
    raise Exception("No Input Data")
lines.remove("")
rules = {}
counter = 0
e = []
z = []
liste = []
parents = ["shinygold"]
parent = "shinygold"
countedParents = []
commander = 1

for i in lines:
    e = []
    z = i.split(" bags contain ")
    h = z[1].split(", ")
    for f in h:
        if not f.startswith("1"):
            y = f.replace(" bags", "")
        else:
            y = f.replace(" bag", "")
        y = y.replace(y[0:2], "")
        y = y.replace(" ", "")
        e.append(y)
    for f in e:
        r = z[0].replace(" ", "")
        r = r.replace("\n", "")
        liste.append(r)
        if f in rules.keys():
            y = rules[f]
            y.append(r)
            rules[f] = y
        if not f in rules.keys():
            rules[f] = liste
        liste = []
while 0 < len(parents):
    parent = parents[0]
    if parent not in countedParents:
        for i in rules.keys():
            if i == parent:
                l = len(rules[parent])
                for e in range(len(rules[parent])):
                    parents.append(rules[parent][e])
        countedParents.append(parent)
    parents.remove(parents[0])
print("The answer is : " + str(len(countedParents)-1))
