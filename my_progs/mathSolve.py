import itertools

print("Starting filling up <stuff> array...")

stuff = []
for i in range(12):
    stuff.append(i+1)
for i in range(12):
    stuff.append(i+1)
for i in range(12):
    stuff.append(i+1)


print("Done filling <stuff> array")

combinationsToCheck = []

print("\nStarting fillig up <combiantionsToCheck>...")

for L in range(0, len(stuff)+1):
    for subset in itertools.combinations(stuff, L):
        if len(subset) == 3:
            new3nums = []
            for j in subset:
                new3nums.append(j)
            combinationsToCheck.append(sorted(new3nums))
        elif len(subset) <3:
            continue 
        else:
            break

print("Done filling up <combiantionsToCheck>")


answers = []

print("Starting checking for answers")

combinationsToCheckFinal = []
for i in combinationsToCheck:
    if i not in combinationsToCheckFinal:
        combinationsToCheckFinal.append(i)

for i in combinationsToCheckFinal:
    if (i[0] + i[1] + i[2] == 14) and (i[0] * i[1] * i[2] == 72):
        # print(str(i[0]) + "+" + str(i[1]) + "+" + str(i[2]) + " == 14\n"+ str(i[0])+"*"+str(i[1])+"*"+str(i[2])+" == 72")
        answers.append(str(i[0]) + "+" + str(i[1]) + "+" + str(i[2]) + " == 14\n"+ str(i[0])+"*"+str(i[1])+"*"+str(i[2])+" == 72")
        print("Answer found")

print("====================================")

for i in answers:
    print("------------")
    print(i)