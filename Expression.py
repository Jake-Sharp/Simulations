import random
deck = []
suits = ["♠", "♥", "♦", "♣"]
for i in range(4):
    suit = ""
    for j in range(1,14):
        value = str(j)
        suit = suits[i]
        if(j == 1):
            value = "A"
        elif(j == 11):
            value = "J"
        elif(j == 12):
            value = "Q"
        elif(j == 13):
            value = "K"
        deck.append(f"{value}{suit}")
print("Regular Deck: ")
print(deck)

def randomize (arr, n): 
    for i in range(n-1,0,-1): 
        j = random.randint(0,i+1) 
        arr[i],arr[j] = arr[j],arr[i] 
    return arr 
n = len(deck)
print("Shuffled Deck: ")
print(randomize(deck, n)) 
