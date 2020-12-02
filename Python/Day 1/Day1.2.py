f = open("Day1.2Input.txt", "r")
inputNumbers = f.read().split("\n")
valid = False
for i in range(len(inputNumbers)):
    for z in range(len(inputNumbers)):
        for x in range(len(inputNumbers)):
            if int(inputNumbers[i])+int(inputNumbers[z])+int(inputNumbers[x]) == 2020:
                Wert = True
                print(inputNumbers[i])
                print(inputNumbers[z])
                print(inputNumbers[x])
                print(int(inputNumbers[i])*int(inputNumbers[z])*int(inputNumbers[x]))
                break
            else:
                valid = False
        if valid == True:
            break
    if valid == True:
        break