import time
start = time.time()
f = open("Day1.1Input.txt", "r")
Zahlen = f.read().split("\n")
Wert = False
for i in range(len(Zahlen)):
    for z in range(len(Zahlen)):
        if int(Zahlen[i])+int(Zahlen[z]) == 2020:
            Wert = True
            print(Zahlen[i])
            print(Zahlen[z])
            print(int(Zahlen[i])*int(Zahlen[z]))
            break
        else:
            Wert = False
    if Wert == True:
        break
end = time.time()
print(end-start)
