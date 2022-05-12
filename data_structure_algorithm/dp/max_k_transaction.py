'''
maximum k transaction
prices = [5,11,3,50,60,90]
k = 2
find the maximum profit
'''


prices = [5,11,3,50,60,90]
k = 2

# create a profit table
def max_k_transaction(prices,k):
    if not len(prices):
        return 0
    profit = [[0 for d in range(len(prices))] for t in range(k+1)]
    for t in range(1,k+1):
        maxsofar = -1e7
        for d in range(1,len(prices)):
            maxsofar = max(maxsofar,profit[t-1][d-1]-prices[d-1])
            profit[t][d] = max(profit[t][d-1],maxsofar+prices[d] )
    print(profit[-1][-1])

max_k_transaction(prices,k)