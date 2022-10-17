# 5 x 5 matrix
'''
[['a','g','n'.'i','k'],
['a','g','n'.'i','k'],
['a','g','n'.'i','k'],
['a','g','n'.'i','k'],
['a','g','n'.'i','k']]
'''
mat = [['a','g','n','i','k'],
        ['a','s','h','i','k'],
        ['a','n','h','i','k'],
        ['a','g','n','i','r'],
        ['a','n','k','i','t']]
def isBingo(mat, pat):
    r,c = 5,5
    # check rows
    for i in range(r):
        if "".join(mat[i][::-1]) == pat or "".join(mat[i]):
            return True
    
    # check columns
    for i in range(0,r):
        for j in range(0,c):
            print(mat[j][i],end=" ")
        print(" ")
    
    diag = c
    rev=0
    i=0
    j=0

    while(diag):
        print(mat[i][j],end=" ")
        i += 1
        j += 1
        diag -= 1

    diag = c
    i=0
    j=4

    while(diag):
        print(mat[i][j],end=" ")
        i += 1
        j -= 1
        diag -= 1


isBingo(mat,"drfgt")
