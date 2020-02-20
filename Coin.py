import random

numFlips = int(input("How many flips? "))

flips = [0] * numFlips
heads = 0
tails = 0
runsFound = 0

for i in range(numFlips):
    flip = random.randint(0,1)
    flips[i] += flip

for i in range(len(flips)):
    if(flips[i] == 1):
        tails+=1
    elif(flips[i] == 0):
        heads+=1

print(f"{heads} Heads {heads/numFlips*100}%, {tails} Tails {tails/numFlips*100}%")

#flips = [0,0,0,1,1,1,0,0,1,1,0,1]
lookFor = int(input("Which side are you looking for (1-tails, 0-heads)? "))
if(lookFor == 1):
    notSearch = 0
elif(lookFor == 0):
    notSearch = 1
run = int(input("How long is the run you're looking for? "))
for i in range(len(flips)):
    if(flips[i:i+run+1] == [lookFor]*run+[notSearch]):
        runsFound+=1

print(flips[0:numFlips])
print(f"Heads shows up {run} times in a row, {runsFound} times")
