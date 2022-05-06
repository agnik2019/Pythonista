mapping = {
    "2":"abc",
    "3":"def",
    "4":"ghi",
    "5":"jkl",
    "6":"mno",
    "7":"pqrs",
    "8":"tuv",
    "9":"wxyz"
}

# input -> digits (23)
# combo ->  [ad,ae,af,bd,be,bf,cd,ce,cf]

def letterComboRec(digits,combo, index):
    if index == len(digits):
        print(combo)
    else:
        for c in mapping[digits[index]]:
            combo += c
            letterComboRec(digits,combo,index+1)
            combo = combo[:-1]

def letterCombo(digits):
    combo = ""
    letterComboRec(digits,combo,0)

letterCombo("23")