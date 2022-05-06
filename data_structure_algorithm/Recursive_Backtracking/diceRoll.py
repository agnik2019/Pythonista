
def diceRollHelper(dices,chosen):
    if dices == 0:
        print(chosen)
    
    else:
        for i in range(1,7):
            chosen.append(i)
            diceRollHelper(dices-1, chosen)
            chosen.pop()

def diceRoll(dices): 
    chosen = []
    diceRollHelper(dices,chosen)

diceRoll(2)