from django.shortcuts import render

# Create your views here.
from random import *
l=[]
def housiecoins():
    while True:
        val=randint(1,90)
        global l
        if val not in l:
            l.append(val)
        if len(l)==90:
            break
i=0
def house(request):
    housiecoins()
    global l,i
    if i>=90:
        val="completed"
    else:
        val=l[i]
    i=i+1
    return render(request,"HousieCoins/Coins.html",{"value":val})

    
