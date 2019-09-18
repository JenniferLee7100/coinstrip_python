import random

#Make the Strip
notValidLength = True
while notValidLength:
    length = int(input("What is the Strip Length?: "))
    if length <= 1:
        print("Not a valid strip length")
    else:
        notValidLength=False
strip=[]
i = 0
while i < length:
    strip.append(0)
    i+=1

#Insert the Coins 
notValidNum = True 
while notValidNum:
    numCoins = int(input("How Many Coins?: "))
    if numCoins<=0 or numCoins>=length:
        print("Not a valid number of coins")
    else: 
        notValidNum = False

coin = 1
while coin<=numCoins-1:
    rand = random.randint(0,length-2)
    if strip[rand]==0 and rand>0:
        strip[rand] = coin
        coin+=1

#Make sure the last box of the strip always has a coin 
strip[len(strip)-1]=numCoins

#Print the strip
def printStrip(strip):
        i=0
        while i < len(strip)-1:
            print("+---+", end =" ")
            i+=1
        print("+---+")
        i=0
        while i < len(strip)-1:
            print("| "+str(strip[i])+" |", end =" ")
            i+=1
        print("| "+str(strip[len(strip)-1])+" |")
        i=0
        while i < len(strip)-1:
            print("+---+", end =" ")
            i+=1
        print("+---+")

printStrip(strip)

#Check if it's a valid coin 
def validCoin(strip,name,numCoins):
    v = True
    while v: 
        v = False
        vCoin = int(input(name+", what coin will you move?: "))
        if vCoin>numCoins or vCoin<=0:
            print("Illegal Move: Invalid Coin")
            v = True
        else: 
            i = 0 
            while i < len(strip):
                if(strip[i]==vCoin):
                    index = i 
                    if(i==0 or strip[i-1]>0):
                        print("Illegal Move: You can't move this coin!")
                        v = True
                        break 
                i+=1
    return index

#Check if a move is valid and if it is, move it 
def validMove(strip, name, coinSpot):
    #Check if it's a valid move
        v = True
        while v: 
            v = False
            vMove = int(input(name+", how many spaces will you move?: "))
            if(vMove<0):
                print("Illegal Move: Invalid movement")
                v = True
            elif coinSpot-vMove < 0:
                print("Illegal Move: Off the Strip")
                v = True
            elif strip[coinSpot-vMove]>0:
                print("Illegal Move: Coin already present")
                v = True
            else:
                #print(coinSpot-vMove) 
                i = coinSpot-vMove
                while i<coinSpot:
                    if strip[i] > 0:
                        print("Illegal Move: You can't pass a coin")
                        v = True
                    i+=1
                    
        #Move it
        strip[coinSpot-vMove] = strip[coinSpot] 
        strip[coinSpot] = 0 
        printStrip(strip)

#Check if game over 
def isNotOver(strip,numCoins):
    i = 0 
    while i < numCoins:
        if strip[i]==0:
            return True
        i+=1
    return False


#Start the game
NotgameOver = True 
while NotgameOver:
    #Player 1's turn 
    coinSpot = validCoin(strip,"Player 1", numCoins)
    #print(coinSpot)
    validMove(strip,"Player 1",coinSpot)
    if isNotOver(strip,numCoins) == False:
        print("Game Over: Player 1 Wins!")
        break
    #Player 2's Turn 
    coinSpot = validCoin(strip,"Player 2", numCoins)
    validMove(strip,"Player 2",coinSpot)
    if isNotOver(strip,numCoins) == False:
        print("Game Over: Player 2 Wins!")
        break

    NotgameOver = isNotOver(strip,numCoins)

