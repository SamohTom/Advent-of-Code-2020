f = open("Day1.2Input.txt", "r")
inputNumbers = f.read().split("\n")
if len(inputNumbers) == 1:
    raise Exception(" No Input Data")
valid = False
for i in range(len(inputNumbers)):
    for z in range(len(inputNumbers)):
        for x in range(len(inputNumbers)):
            if int(inputNumbers[i])+int(inputNumbers[z])+int(inputNumbers[x]) == 2020:
                valid = True
                print(inputNumbers[i])
                print(inputNumbers[z])
                print(inputNumbers[x])
                print("The answer is : " + str(int(inputNumbers[i])*int(inputNumbers[z])*int(inputNumbers[x])))
                break
            else:
                valid = False
        if valid == True:
            break
    if valid == True:
        break