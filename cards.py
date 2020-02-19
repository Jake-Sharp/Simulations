import random

def bubble_sort(arr):
    n = len(arr)
    s={"♠":0,"♥":1,"♦":2,"♣":3}
    f={"A":1,"J":11,"Q":12,"K":13}
   
    for i in range(n):
        for j in range(0, n-i-1):
            a = arr[j]
            b = arr[j+1]

            aface  = arr[j][0:len(a)-1]
            asuit  = arr[j][len(a)-1]
            avalue = f[aface] if aface in f else int(aface)

            bface  = arr[j+1][0:len(b)-1]
            bsuit  = arr[j+1][len(b)-1]
            bvalue = f[bface] if bface in f else int(bface)

            if (asuit > bsuit):
                arr[j], arr[j+1] = arr[j+1], arr[j]
            elif (asuit == bsuit):
                if (avalue > bvalue):
                    arr[j], arr[j+1] = arr[j+1], arr[j]
def shuffle(arr):
    n = len(arr)
    for i in range(n-1,0,-1): 
        j = random.randint(0,i+1) 
        arr[i],arr[j] = arr[j],arr[i]

def deal():
    d=[]
    s=["♠","♥","♦","♣"]
    f={1:"A",11:"J",12:"Q",13:"K"}
    for i in range(4):
        for j in range(1,14):
            d.append(f"{f[j] if j in f else j}{s[i]}")
    return d

###

cards = deal()
print("Before shuffle: ")
print(cards)

shuffle(cards)
print("After shuffle: ")
print(cards)
