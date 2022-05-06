'''
Write a function printMovieOrders that accepts a Vector of
movie names (Strings) as a parameter and outputs all possible
orders in which we could watch those movies.
Input: 
    movies = ["RRR","KGF","Pushpa","Bahubali"]
output:

['RRR', 'KGF', 'Pushpa', 'Bahubali']
['RRR', 'KGF', 'Bahubali', 'Pushpa']
['RRR', 'Pushpa', 'KGF', 'Bahubali']
['RRR', 'Pushpa', 'Bahubali', 'KGF']
['RRR', 'Bahubali', 'KGF', 'Pushpa']
['RRR', 'Bahubali', 'Pushpa', 'KGF']
['KGF', 'RRR', 'Pushpa', 'Bahubali']
['KGF', 'RRR', 'Bahubali', 'Pushpa']
['KGF', 'Pushpa', 'RRR', 'Bahubali']
['KGF', 'Pushpa', 'Bahubali', 'RRR']
['KGF', 'Bahubali', 'RRR', 'Pushpa']
['KGF', 'Bahubali', 'Pushpa', 'RRR']
['Pushpa', 'RRR', 'KGF', 'Bahubali']
['Pushpa', 'RRR', 'Bahubali', 'KGF']
['Pushpa', 'KGF', 'RRR', 'Bahubali']
['Pushpa', 'KGF', 'Bahubali', 'RRR']
['Pushpa', 'Bahubali', 'RRR', 'KGF']
['Pushpa', 'Bahubali', 'KGF', 'RRR']
['Bahubali', 'RRR', 'KGF', 'Pushpa']
['Bahubali', 'RRR', 'Pushpa', 'KGF']
['Bahubali', 'KGF', 'RRR', 'Pushpa']
['Bahubali', 'KGF', 'Pushpa', 'RRR']
['Bahubali', 'Pushpa', 'RRR', 'KGF']
['Bahubali', 'Pushpa', 'KGF', 'RRR']
'''
def movieOrderRec(allMovies,chosen):
    if len(allMovies) == 0:
        print(chosen)
    for i in range(len(allMovies)):
        currMovie = allMovies[i]
        allMovies.pop(i)
        chosen.append(currMovie)  # choose
        movieOrderRec(allMovies,chosen)  # explore
        chosen.pop()    # unchoose
        allMovies.insert(i,currMovie)

def printMovieOrders(movies):
    chosen = []
    movieOrderRec(movies,chosen)


def main():
    movies = ["RRR","KGF","Pushpa","Bahubali"]
    printMovieOrders(movies)


main()