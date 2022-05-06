
def diceRollHelper(dices,chosen,desiredSum):
    if dices == 0:
        if sum(chosen) == desiredSum:
            print(chosen)
    
    else:
        for i in range(1,7):
            chosen.append(i)
            diceRollHelper(dices-1, chosen,desiredSum)
            chosen.pop()

def diceRoll(dices,desiredSum): 
    chosen = []
    diceRollHelper(dices,chosen,desiredSum)

diceRoll(2,7)