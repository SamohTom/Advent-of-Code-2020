f = open("Day1.1Input.txt", "r")
inputNumbers = f.read().split("\n")
valid = False
for i in range(len(inputNumbers)):
    for z in range(len(inputNumbers)):
        if int(inputNumbers[i])+int(inputNumbers[z]) == 2020:
            valid = True
            print(inputNumbers[i])
            print(inputNumbers[z])
            print(int(inputNumbers[i])*int(inputNumbers[z]))
            break
        else:
            valid = False
    if valid:
        break

