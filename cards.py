import random
import sys 

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
print("Start Deck: ")
print(deck)



def randomize (arr):
    n = len(arr)
    for i in range(n-1,0,-1): 
        j = random.randint(0,i+1) 
        arr[i],arr[j] = arr[j],arr[i] 
    return arr 

print("Shuffled Deck: ")
print(randomize(deck))

def bubble_sort(arr):
    n = len(arr)
    s={"♠":0,"♥":1,"♦":2,"♣":3}
    f={"A":1,"J":11,"Q":12,"K":13}
    
    for i in range(n):
        for j in range(0, n-i-1):
            x = arr[j]
            y = arr[j+1]

            xf  = x[0:len(x)-1];
            xs  = x[len(x)-1];
            xv = f[xf] if xf in f else int(xf)

            yf  = b[0:len(b)-1];
            ys  = b[len(b)-1];
            yv = f[bface] if bface in f else int(bface)

            if (xs > ys or (xs == ys and xv > yv)):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
def selectionSort(arr):
    f={"A":1,"J":11,"Q":12,"K":13}
    n = len(arr)
    for i in range(n): 
        min_crd = i 
        for j in range(i+1, len(arr)):
            x = arr[min_crd]
            y = arr[j]
            xf = x[0:len(x)-1]
            xs = x[len(x)-1]
            xv = f[xf] if xf in f else int(xf)

            yf = y[0:len(y)-1]
            ys = y[len(y)-1]
            yv = f[yf] if yf in f else int(yf)

            if (xs > ys or (xs == ys and xv > yv)):
                min_crd = j
        arr[i], arr[min_crd] = arr[min_crd], arr[i]
  
selectionSort(deck)
print("Sorted Deck: ")
print(deck)
