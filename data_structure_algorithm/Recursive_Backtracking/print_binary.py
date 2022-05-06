"""
printBinary(2):
"00"
"01"
"10"
"11"

"""

def printBinaryHelper(digits, soFar):
    if digits == 0:
        print(soFar)
    else:
        printBinaryHelper(digits-1, soFar+'0')
        printBinaryHelper(digits-1, soFar+'1')

def printBinary(digits):
     printBinaryHelper(digits,'')

def main():
    printBinary(4)

main()