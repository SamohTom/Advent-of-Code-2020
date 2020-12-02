import time
start = time.time()
f = open("Day1.2Input.txt", "r")
Zahlen = f.read().split("\n")
Wert = False
for i in range(len(Zahlen)):
    for z in range(len(Zahlen)):
        for x in range(len(Zahlen)):
            if int(Zahlen[i])+int(Zahlen[z])+int(Zahlen[x]) == 2020:
                Wert = True
                print(Zahlen[i])
                print(Zahlen[z])
                print(Zahlen[x])
                print(int(Zahlen[i])*int(Zahlen[z])*int(Zahlen[x]))
                break
            else:
                Wert = False
        if Wert:
            break
    if Wert:
        break
end = time.time()
print(end-start)
