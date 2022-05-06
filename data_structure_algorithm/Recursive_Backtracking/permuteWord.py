def permuteRec(Remaining,soFar):
    if len(Remaining) == 0:
        print(soFar)
    else:
        for i in range(len(Remaining)):
            nextLetter = Remaining[i]
            rest = Remaining[:i]+Remaining[i+1:]
            permuteRec(rest,soFar+nextLetter)

def permute(word):
    sofar=""
    permuteRec(word,sofar)

permute("cat")

'''
cat
cta
act
atc
tca
tac
'''